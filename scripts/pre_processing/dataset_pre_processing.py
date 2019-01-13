import pandas as pd
import numpy as np


def create_data_set(signals, annotations):
    print('Creating data-set...')

    print(list(signals))
    print(list(annotations))

    data_set = pd.merge_asof(signals[['Datetime', 'F2-F4[uV]', 'F4-C4[uV]', 'F1-F3[uV]']],
                             annotations[['Datetime', 'Sleep Stage', 'Event', 'Duration[s]']],
                             left_on='Datetime', right_on='Datetime', by='Datetime')

    print('Creating data-set...Done')
    return data_set


def fill_data_set(data_set):
    print('Filling data-set...')
    # data_set = data_set.c(method='ffill', inplace=True)

    # Fill the empty rows of the 'Event' column with the previous value
    data_set[data_set['Event'] == ""] = np.NaN
    data_set.fillna(method='ffill')
    print(data_set)

    # Drop data that have no annotations
    # data_set['Event'].dropna()

    print('Filling data-set...Done')


def find(signals, annotations):
    print('Find...')

    j = 0
    an = []
    for i in range(1, len(annotations['Time [hh:mm:ss]'])):
        while signals['Time [hh:mm:ss]'][j] != annotations['Time [hh:mm:ss]'][i]:
            an.append(annotations['Duration[s]'][i - 1])
        j = j + 1
        print(j, ' ', i, ' ', annotations['Duration[s]'][i - 1])
        an.append(annotations['Duration[s]'][i])
        j = j + 1

    signals['Scoring'] = an
    d1 = an

    signals['Scoring'] = d1
    signals['Scoring'].to_csv('d1', index=False)

    signals.to_csv('D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\whole_dataset', index=False)
    signals = signals.drop(['Unnamed: 0', 'HH', 'MM', 'SS'], axis=1)
    # Rearrange columns
    signals = signals[['Date', 'Time [hh:mm:ss]', 'F4-C4[uV]', 'F3-C3[uV]', 'Scoring']]

    signals.to_csv('D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\final.csv', index=False)

    signals = signals.drop(['Date', 'Time [hh:mm:ss]', 'Scoring'], axis=1)
    signals.to_csv('Professor', index=False, header=None)

    list(signals['Time [hh:mm:ss]']).index('07:34:13')
