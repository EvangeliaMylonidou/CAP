import pandas as pd
import numpy as np
import mne


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

    signals = _create_signal_datetime_structure(signals)

    '''
    # Change the sampling frequency
    signals = _re_sampling(file_name, len(signals))

    # Apply band-pass filter.
    raw_object = _apply_band_pass_filter(signals)
    print(raw_object)
    '''
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
    signals = pd.read_csv(file_name, sep='\t')

    print('\tLoad signals file...Done')
    return signals


def _create_signal_datetime_structure(signals):
    print('\tCreating signal datetime structure...')

    # Modify the time and change it to HH:MM:SS format.
    time = _concatenate_signal_time(signals[['HH', 'MM', 'SS']])

    # Combine Date and Time in one column.
    date_time = _concatenate_signal_date_and_time(signals['Date'], time)

    # Insert column Datetime in the first column of the DataFrame
    signals.insert(loc=0, column='Datetime', value=date_time)

    # Delete columns Date, 'HH', 'MM', 'SS'] because they are no longer needed,
    # they are replaced with the column: Datetime
    signals.drop(columns=['Date', 'HH', 'MM', 'SS'], axis=1, inplace=True)

    print('\tCreating signal datetime structure...Done')
    return signals


def _concatenate_signal_date_and_time(signals_dates, time):
    print('\t\tConcatenate signal date and time...')
    date_time = ["{} {}".format(date_, time_) for date_, time_ in zip(signals_dates, time)]

    print('\t\tConcatenate signal date and time...Done')
    return date_time


def _concatenate_signal_time(signals_time):
    print('\t\tConcatenate signal time structure...')

    hours = signals_time.iloc[:, 0].values
    minutes = signals_time.iloc[:, 1].values
    seconds = signals_time.iloc[:, 2].values

    time = ["{}:{}:{}".format(hour_, minute_, second_) for hour_, minute_, second_ in zip(hours, minutes, seconds)]

    time = pd.Series(pd.to_datetime(time, format='%H:%M:%S.%f'), index=None).dt.strftime('%H:%M:%S')

    print('\t\tConcatenate signal time structure...Done')
    return time


def _re_sampling(file_name, signals_length):
    print('\tRe-sampling...')
    # Change sampling frequency from 512Hz to 128Hz -> 512/4 = 128.
    skip_rows = [row for row in range(signals_length) if row % 4 != 0]

    # Load signals file again but with skipping the above mentioned rows.
    signals = pd.read_csv(file_name, sep='\t', skiprows=skip_rows)

    print('\tRe-sampling...Done')
    return signals


def _apply_band_pass_filter(signals):
    print('\tApplying Band-Pass Filter...')

    # Apply band-pass filter
    signals_array = np.array([signals['F2-F4[uV]'], signals['F4-C4[uV]'], signals['F1-F3[uV]']])

    # Create a list with the channel names
    channel_names = ['F2-F4[uV]', 'F4-C4[uV]', 'F1-F3[uV]']
    # Channel types are all EEG
    channel_types = 'eeg'
    # Sampling rate
    sampling_frequency = 128  # Hz

    # Create the info-structure needed for our object with MNE
    info_structure = mne.create_info(ch_names=channel_names, sfreq=sampling_frequency, ch_types=channel_types)

    # Create raw object
    # Band-pass filter, it takes frequencies from 0.05 - 30Hz.
    raw = mne.io.RawArray(signals_array, info_structure).filter(0.05, 30)

    print('\tApplying Band-Pass Filter...Done')
    return raw
