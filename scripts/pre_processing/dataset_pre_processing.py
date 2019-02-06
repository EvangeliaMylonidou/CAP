import numpy as np
import pandas as pd


def create_data_set(signals, annotations):
    # Windowing every 2 minutes with 1 minute overlap.
    dataset = _windowing(signals, annotations)

    # Windowing every 2 minutes without overlap.

    return dataset


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


def _windowing3341(signals, annotations):
    print('\tWindowing...')
    print(signals.__len__())

    np_signals = np.asanyarray(signals)

    window_size = 200
    overlap_size = int(window_size / 2)

    dataset = []

    for w in range(0, len(signals), overlap_size):

        if w + window_size - 1 > len(signals):
            pass

        window = np_signals[w: w + window_size - 1, 1:]

        window_array = np.reshape(window, -1)
        print('{} == {}'.format(np_signals[w][0], np_signals[w + window_size - 1][0]))

        if np_signals[w][0] is np_signals[w + window_size - 1][0]:
            print('annotations["Datetime"].__contain__(signals[w]) == {}'
                  .format(annotations['Datetime'].__contains__(signals[w][0])))
            if annotations['Datetime'].__contains__(signals[w][0]):
                print(annotations['Date']['Event'])
            else:
                print('In else: ', annotations['Date']['Event'])

            # Check if the first signal's datetime is the same with the last signal's.
            # if not np_signals[first_window_signal][0] == np_signals[last_window_signal][0]:
            #    print(annotations['Datetime'][0])
            #    print(np_signals[first_window_signal][0])
            #    print('annotations["Datetime"].__contains__(signals[w]) == {}'
            #          .format(annotations['Datetime'][0].__contains__(np_signals[first_window_signal][0])))
    # If so, check if the annotation date-times contain the signal's datetime
    # if annotations['Datetime'].__contains__(np_signals[first_window_signal][0]):
    #
    #   print(list(annotations))
    #   print(annotations.loc[annotations['Date'] == np_signals[first_window_signal][0]]['Event'])
    #   annotation = annotations.loc[annotations['Date'] == np_signals[first_window_signal][0]]['Event']

    # else:
    #    print('In else: ', annotations['Datetime']['Event'])

    # print('window: ', dataset)
    dataset.append((window_array, 'dada'))

    for d in dataset:
        print(d)

    print('\tWindowing...Done')
    return dataset


def _windowing(signals, annotations):
    """
    Separates the signals in overlapping windows and gives each signal the appropriate annotation.
    In the meantime, it saves each window and its annotation in a Numpy array.

    :param signals: A DataFrame containing all the signals
    :param annotations: A DataFrame containing all the annotations
    :return: dataset: A DataFrame / Numpy array with the windowed and annotated signals
    """
    print('\tWindowing...')

    # Convert signal DataFrame to numpy array
    np_signals = np.asanyarray(signals)

    # Set the window and overlap sizes: window = 200, overlap = 100
    window_size = 200
    overlap_size = int(window_size / 2)

    # Initialize the dataset and window lists
    dataset = []
    window_array = []

    # Iterate through every set of signals, with step equal to the overlap size
    for first_window_signal in range(0, len(np_signals) - 1, overlap_size):

        last_window_signal = first_window_signal + window_size - 1
        # Check if the iteration has gone above the array limits.
        if last_window_signal > len(np_signals) - 1:
            # If so, just use all the rest signals.
            last_window_signal = len(np_signals) - 1

        # Set the window signals and reshape the array in order to be one row instead of one column.
        window = np_signals[first_window_signal:last_window_signal, 1:]
        window_array = np.reshape(window, -1)

        print(np_signals[first_window_signal][0], '---', np_signals[last_window_signal][0])

        date = np_signals[0][0]

        dataset.append((date, window_array))

    print('\tWindowing...Done')
    return dataset
