import numpy as np
import pandas as pd

from scipy import signal
from scripts.pre_processing.signal_time_structure \
    import create_datetime_structure, _to_timestamp, _to_datetime


SIGNAL_COLUMNS = ['Date', 'HH', 'MM', 'SS', 'F2-F4[uV]', 'F4-C4[uV]', 'F1-F3[uV]']


def load_signals(file_name):
    """
    Loads signals and calls all the functions needed to manipulate the signals
    and change them in the way is fits us better.
    :param file_name: CSV file containing all the signals.
    :return: DataFrame with the manipulated signals.
    """
    print('Loading signals...')

    # Load the signals from a file and save them into a DataFrame.
    signals = _load_signals(file_name)

    # Change the signal datetime structure and return the changed DataFrame
    signals = _create_datetime_structure(signals)

    # Change the sampling frequency
    signals = _re_sampling(signals)

    # Windowing every 2 minutes with 1 minute overlap.
    # _windowing(signals)

    # Windowing every 2 minutes without overlap.

    print('Loading signals...Done')
    return signals


def _load_signals(file_name):
    """
    Loads and returns the signals by extracting them from a CSV file.
    :param file_name: CSV file containing all the signals.
    :return: DataFrame with the extracted signals.
    """
    print('\tLoad signals file...')

    # Load the signals from a file and save them into a DataFrame.
    signals = pd.read_csv(file_name, sep='\t', usecols=SIGNAL_COLUMNS, nrows=135000)

    print('\tLoad signals file...Done')
    return signals


def _re_sampling(signals):
    print('\tRe-sampling...')

    print(signals)
    signals['Datetime'] = _to_timestamp(signals['Datetime'])

    freq_100_hz = 512 / 100
    total_amount_of_signals = len(signals) / freq_100_hz

    re_sampled_data = signal.resample(signals, int(total_amount_of_signals))

    signals = pd.DataFrame(re_sampled_data, columns=list(signals))

    signals['Datetime'] = _to_datetime(signals['Datetime'])
    print(signals)

    print('\tRe-sampling...Done')
    return signals


def _re_sampling_with_shuffle(signals):
    print('\tRe-sampling...')

    freq_100_hz = 512 / 100
    total_amount_of_signals = len(signals) / freq_100_hz

    re_sampled_data = []  # resample(signals)

    print(signals.__len__(), re_sampled_data.__len__())
    print(re_sampled_data)

    print('\tRe-sampling...Done')
    return re_sampled_data


data = [['1996/07/03 11:40:35', -23.3455, 24.5534, -325.653],
        ['1996/07/03 11:40:35', 23.3465, -24.5444, 325.653],
        ['1996/07/03 11:40:35', -23.3455, -24.5564, 325.653],
        ['1996/07/03 11:40:36', 23.3455, 24.5534, 325.666],
        ['1996/07/03 11:40:36', -23.3444, -24.5534, -3254.653],
        ['1996/07/03 11:40:36', 23.3456, 24.5534, 325.653],
        ['1996/07/03 11:40:36', -23.3455, 24.5534, -325.653]]
dataset = pd.DataFrame(data, columns=['datetime', 'f1-f2', 'f2-f3', 'f3-f4'])


def _windowing(signals):
    print('\tWindowing...')
    print(signals.__len__())

    window_size = 200
    overlap_size = window_size/2

    for w in range(len(signals)):
        window = signals.loc[w:window_size, :]

    print(window, window.__len__())
    print('\tWindowing...Done')


def _create_datetime_structure(signals):
    return create_datetime_structure(signals)
