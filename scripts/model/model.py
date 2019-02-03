import sklearn.model_selection as sk


def cross_validation(X, t, folds=10):
    print('{}-fold Cross-Validation...'.format(folds))

    for fold in range(folds):
        # Split train and test sets...
        X_train, X_test, t_train, t_test = sk.train_test_split(X, t, test_size=0.1)

    print('{}-fold Cross-Validation...Done'.format(folds))
    return X_train, X_test, t_train, t_test


