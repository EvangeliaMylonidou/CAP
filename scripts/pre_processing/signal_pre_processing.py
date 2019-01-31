import pandas as pd


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
    # signals = _re_sampling(signals)

    # date_time = _convert_timestamp_to_datetime(signals['Datetime'])
    # signals['Datetime'] = date_time

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


def _create_datetime_structure(signals):
    print('\tCreating signal datetime structure...')

    # Modify the time and change it to HH:MM:SS format.
    time = _concatenate_time(signals[['HH', 'MM', 'SS']])

    # Combine Date and Time in one column.
    date_time = _concatenate_date_and_time(signals['Date'], time)

    # Insert column Datetime in the first column of the DataFrame
    signals.insert(loc=0, column='Datetime', value=date_time)

    # Delete columns Date, 'HH', 'MM', 'SS'] because they are no longer needed,
    # they are replaced with the column: Datetime
    signals.drop(columns=['Date', 'HH', 'MM', 'SS'], axis=1, inplace=True)

    print('\tCreating signal datetime structure...Done')
    return signals


def _concatenate_time(signals_time):
    print('\t\tConcatenate signal time structure...')

    hours = signals_time.iloc[:, 0].values
    minutes = signals_time.iloc[:, 1].values
    seconds = signals_time.iloc[:, 2].values

    time = ["{}:{}:{}".format(hour_, minute_, second_) for hour_, minute_, second_ in zip(hours, minutes, seconds)]

    time = pd.Series(pd.to_datetime(time, format='%H:%M:%S.%f'), index=None).dt.strftime('%H:%M:%S')

    print('\t\tConcatenate signal time structure...Done')
    return time


def _concatenate_date_and_time(signals_dates, time):
    print('\t\tConcatenate signal date and time...')
    date_time = ["{} {}".format(date_, time_) for date_, time_ in zip(signals_dates, time)]

    print('\t\tConcatenate signal date and time...Done')
    return date_time

