import pandas as pd
import numpy as np


def load_data_set(signals, annotations):
    print('Loading data-set...')
    data_set = _create_data_set(signals=signals, annotations=annotations)
    data_set = _fill_data_set(data_set)

    print(data_set)
    print('Loading data-set...Done')
    return data_set


def _create_data_set(signals, annotations):
    print('Creating data-set...')

    signals['Datetime'] = pd.to_datetime(signals.Datetime)
    annotations['Datetime'] = pd.to_datetime(annotations.Datetime)
    data_set = pd.merge_asof(left=signals, right=annotations, on='Datetime')

    print('Creating data-set...Done')
    return data_set


def _create_data_set2(signals, annotations):
    print('Creating data-set...')

    t = pd.Series()

    for signal in range(107519, len(signals['Datetime'])):

        for annotation in range(len(annotations['Datetime'])):
            print(signals['Datetime'][signal], ' == ', annotations['Datetime'][annotation])
            if signals['Datetime'][signal] == annotations['Datetime'][annotation]:
                print('signal = {}, annotation = {}'.format(signal, annotation))
                print('t = ', annotations['Event'][annotation])
                print(signal)
                t.append(annotations['Event'][annotation])
            break

    signals['Event'] = pd.Series(t, index=signals.index)
    print(signals.head())

    print('Creating data-set...Done')
    return signals


def _fill_data_set(data_set):
    print('Filling data-set...')

    # Replace the empty cells of the 'Event' column with NaNs
    data_set[data_set['Event'] == ''] = np.NaN

    # Fill the empty cells of the 'Event' column with the previous value
    data_set.fillna(method='ffill')

    # Drop data that have no annotations
    data_set = data_set.dropna()

    print('Filling data-set...Done')
    return data_set
