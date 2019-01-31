import pandas as pd
import numpy as np
import statistics as st

from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

# import imblearn
# from imblearn.over_sampling import SMOTE
# from imblearn.under_sampling import TomekLinks
# from imblearn.combine import SMOTETomek
# from imblearn.under_sampling import ClusterCentroids
# from imblearn.under_sampling import RandomUnderSampler
# from xgboost import XGBClassifier

''' Load data'''
data = pd.read_csv('ML_data_set')

''' Remove the feature stages from the semi automated model '''
data = data.drop(['stages'], axis=1)

''' Built the time sequence feature '''
limit = 4
step = len(data.columns) - 2
data11 = pd.DataFrame(data.iloc[limit - 1:-limit - 1, :-2].values)  # 1 before
data12 = pd.DataFrame(data.iloc[limit + 1:-limit + 1, :-2].values,
                      columns=list(range(len(data.columns) - 1, len(data.columns) - 1 + step)))  # 1 front
data21 = pd.DataFrame(data.iloc[limit - 2:-limit - 2, :-2].values,
                      columns=list(range(len(data.columns) - 1 + step, len(data.columns) - 1 + 2 * step)))  # 2 before
data22 = pd.DataFrame(data.iloc[limit + 2:, :-2].values, columns=list(
    range(len(data.columns) - 1 + 2 * step, len(data.columns) - 1 + 3 * step)))  # 2 front
data31 = pd.DataFrame(data.iloc[limit - 2:-limit - 2, :-2].values, columns=list(
    range(len(data.columns) - 1 + 3 * step, len(data.columns) - 1 + 4 * step)))  # 3 before
data32 = pd.DataFrame(data.iloc[limit + 2:, :-2].values, columns=list(
    range(len(data.columns) - 1 + 4 * step, len(data.columns) - 1 + 5 * step)))  # 3 front

data = data.iloc[limit:-limit, :-2].join([data11, data12, data21, data22,
                                          data31, data32, data.iloc[limit:-limit, -2:]])

''' Encode the stage feature from the semi automated model '''
# import category_encoders as ce
#
# encoder = ce.OneHotEncoder(cols=['stages'])
# data = encoder.fit_transform(data)

''' Fill Nan values with zero '''
data = data.replace(np.inf, 0)
data = data.replace(np.nan, 0)

''' Define the classifier '''
clf1 = ExtraTreesClassifier(n_estimators=900, max_depth=300,
                            min_samples_split=2, random_state=0, verbose=3, n_jobs=4)

''' Start the loop for the 10 fold cross validation '''
sensitivity = []
specificity = []
AUC = []
accuracy = []
prev = 0
for limit in range(round(len(data.targets) / 10), len(data.targets), round(len(data.targets) / 10)):

    ''' Define train and test for every fold '''
    X_train = data.drop(list(range(prev, limit)), axis=0)
    data1 = X_train
    y_train = data.drop(list(range(prev, limit)), axis=0)
    y_train = y_train.targets
    data1.targets = y_train
    x_test = data[prev:limit]
    x_test = x_test[x_test.columns[:-1]]
    y_test = data[prev:limit]
    y_test = y_test.targets

    ''' Define the train classes on Non A-phase(c0) vs A-phase(c2)'''
    c0 = data1.loc[data1['targets'] == 'c0']
    # c1=data1.loc[data1['targets'] == 'c1']
    c = data1.loc[data1['targets'] == 'c2']
    # c3=data1.loc[data1['targets'] == 'c3']

    data1 = pd.concat([c0, c])
    data1 = data1.sample(frac=1)
    X_train = data1[data1.columns[:-1]]
    y_train = data1.targets

    nl = []
    for i in y_train:
        if i != 'c0':
            nl.append('c')
        else:
            nl.append('c0')
    y_train = nl

    ''' Grouping Non A-phase with A-phase offsets vs A-phase with A-phase onsets'''
    nl = []
    for i in y_test:
        if i == 'c0':
            nl.append('c0')
        elif i == 'c1':
            nl.append('c')
        elif i == 'c2':
            nl.append('c')
        elif i == 'c3':
            nl.append('c0')
    y_test = nl

    prev = limit

    ''' Train the classifier'''
    clf1.fit(X_train, y_train)

    ''' Oversampling technique SMOTE '''
    #    smt = SMOTETomek(ratio='auto')
    #    X_smt, y_smt = smt.fit_sample(X_train, y_train)
    #
    #    clf1.fit(X_smt, y_smt)

    ''' Predict '''
    y_predict = clf1.predict(x_test)

    ''' Compute evaluating metrics accuracy, sensitivity, specificity, AUC'''
    accuracy.append(accuracy_score(y_test, y_predict))
    #    print('accuracy',accuracy_score(y_test, y_predict))
    # s=pd.Series(y_predclf1)
    # s.unique()

    confusion = metrics.confusion_matrix(y_test, y_predict, labels=['c', 'c0'])
    print(confusion)

    # pd.DataFrame(y_test).groupby(0).size()

    TP = confusion[0][0]
    FP = confusion[0][1]
    FN = confusion[1][0]
    TN = confusion[1][1]

    sens = TP / (TP + FN)
    spec = TN / (TN + FP)

    sensitivity.append(sens)
    specificity.append(spec)

    from sklearn.metrics import roc_auc_score

    nl = []
    for i in y_test:
        if i != 'c0':
            nl.append(1)
        else:
            nl.append(0)
    y_true = nl
    nl = []
    for i in y_predict:
        if i != 'c0':
            nl.append(1)
        else:
            nl.append(0)
    y_scores = nl

    auc = roc_auc_score(y_true, y_scores)
    AUC.append(auc)
    confusion = metrics.confusion_matrix(y_true, y_scores, labels=[1, 0])

print('accuracy', st.mean(accuracy))
print('sensitivity', st.mean(sensitivity))
print('specificity', st.mean(specificity))
print('AUC', st.mean(AUC))
