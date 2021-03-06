import numpy as np
import pandas as pd


def load_data_set(signals, annotations):
    print('Loading data-set...')
    # Windowing every 2 minutes with 1 minute overlap.
    data_set = _windowing_with_overlap(signals)
    # print(data_set.shape)

    # Windowing every 2 minutes without overlap.

    # data_set = _labelling(data_set, annotations)

    '''
    data_set = _create_data_set(signals=signals, annotations=annotations)
    data_set = _fill_data_set(data_set)
    print(data_set)
    '''
    print('Loading data-set...Done')
    return data_set


def _windowing_with_overlap(signals):
    """
    Separates the signals in overlapping windows and gives each signal the appropriate annotation.
    In the meantime, it saves each window and the appropriate date in a Numpy array.

    :param signals: A DataFrame containing all the signals
    :return: data_set: A DataFrame array with the windowed signals
    """
    print('\tWindowing...')

    # Convert signal DataFrame to numpy array
    # # np_signals = np.asanyarray(signals)
    # print('\n---> Signals.shape = ', signals.shape)

    # Set the window and overlap sizes: window = 200, overlap = 100
    window_size = 200
    overlap_size = int(window_size / 2)

    # Initialize the data-set list
    data_set_list = []

    # Iterate through every set of signals, with step equal to the overlap size
    for first_window_signal in range(0, len(signals), overlap_size):

        last_window_signal = first_window_signal + window_size

        # Check if the iteration has gone above the array limits.
        if last_window_signal >= len(signals):
            # If so, just use all the rest signals.
            last_window_signal = len(signals) - 1

        # print('---> first_window_signal = ', first_window_signal)
        # print('---> last_window_signal = ', last_window_signal)
        # print('---> amount = ', last_window_signal - first_window_signal)

        # Set the window signals
        window = signals.ix[first_window_signal:last_window_signal, 1:]
        # print('\n---> Window.shape = ', window.shape)
        # print('\n', window.head(1))
        # print('\n', window.tail(1))
        # # window = np_signals[first_window_signal:last_window_signal, 1:]

        # Reshape the array in order to be one row instead of one column.
        window = pd.DataFrame(window[1:].apply(lambda x: ', '.join(x.astype(str)), axis=0)).transpose()
        # print('---> New Window: \n', window)
        # print('\n---> New Window.shape = ', window.shape)

        # # window_array = np.reshape(window, -1)  # [np.newaxis]
        # # window = np.array((date, window_array))

        # Define the window date as the date of the first signal in the window.
        date = signals.iloc[first_window_signal, 0]
        # print('---> Date: ', date)

        # # window.insert(loc=0, column='Datetime', date)
        # # window['Datetime'] = date
        # print('---> New Window: \n', window)

        # Add the first window signal date and the window array into the data-set
        data_set_list.__add__(window)
        ''' TypeError: can only concatenate list (not "DataFrame") to list '''

    print('---> Dataset List: \n', np.shape(data_set_list))
    # data_set = pd.DataFrame(data_set_list)
    # print('---> Dataset: \n', data_set)

    print('\tWindowing...Done')
    return data_set_list


def _labelling(signals, annotations):
    print('\tLabelling...')

    # signals['Datetime'] = pd.to_datetime(signals.Datetime)
    # annotations['Datetime'] = pd.to_datetime(annotations.Datetime)
    data_set = pd.merge_asof(left=signals, right=annotations, on='Datetime')

    print('\tLabelling...Done')
    return data_set


'''
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
'''


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


def _labeling(annotations, first_signal, last_signal):

    label = ''

    if annotations['Datetime'].any() == first_signal[0]:
        annotation = annotations.loc[[annotations['Datetime'].any() == first_signal[0]]]
        label = annotation['Event']
        print(annotation['Event'])

    elif annotations['Datetime'].any() == last_signal[0]:
        annotation = annotations.loc[[annotations['Datetime'].any() == last_signal[0]]]
        label = annotation['Event']
        print(annotation['Event'])

    date = ''

    return date, label
