import numpy as np
import pandas as pd

from scripts.pre_processing.signal_time_structure import create_datetime_structure


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

    # Change the sampling frequency
    signals = _re_sampling(signals)

    # Change the signal datetime structure and return the changed DataFrame
    signals = _create_datetime_structure(signals)

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

    freq_100_hz = 512 / 100

    re_sampled_data = np.asarray(signals)[0::int(freq_100_hz), :]

    signals = pd.DataFrame(re_sampled_data, columns=list(signals))

    print('\tRe-sampling...Done')
    return signals


def _create_datetime_structure(signals):
    return create_datetime_structure(signals)
