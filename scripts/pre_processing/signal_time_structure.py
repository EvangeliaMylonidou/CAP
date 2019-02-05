from datetime import datetime
import pandas as pd


# ============================== SIGNALS ==============================

def create_datetime_structure(signals):
    print('\tCreating signal datetime structure...')

    # Combine date and time, into a YYYY/MM/DD HH:MM:SS format and place them in one column.
    date_time = _create_datetime(signals[['Date', 'HH', 'MM', 'SS']])

    # Insert column Datetime in the first column of the DataFrame
    signals.insert(loc=0, column='Datetime', value=date_time)

    # Delete columns [Date, 'HH', 'MM', 'SS'] and replace them by the column: Datetime
    signals.drop(columns=['Date', 'HH', 'MM', 'SS'], axis=1, inplace=True)

    print('\tCreating signal datetime structure...Done')
    return signals


def _create_datetime(signal_datetime):
    print('\t\tConcatenating signal datetime...')

    dates = signal_datetime.iloc[:, 0].values
    hours = signal_datetime.iloc[:, 1].values
    minutes = signal_datetime.iloc[:, 2].values
    seconds = signal_datetime.iloc[:, 3].values

    date_time = ["{} {}:{}:{}".format(date_, hour_, minute_, second_)
                 for date_, hour_, minute_, second_ in zip(dates, hours, minutes, seconds)]

    date_time = pd.Series(pd.to_datetime(date_time, format='%Y/%m/%d %H:%M:%S.%f'), index=None)\
        .dt.strftime('%Y/%m/%d %H:%M:%S')

    print('\t\tConcatenating signal datetime...Done')
    return date_time


def _to_timestamp(date_time):
    print('\t\tConverting datetime to timestamp...')

    timestamp = [datetime.strptime(datetime_, '%Y/%m/%d %H:%M:%S').timestamp() for datetime_ in date_time]

    print('\t\tConverting datetime to timestamp...Done')
    return timestamp


def _to_datetime(timestamp):
    print('\t\tConverting datetime to timestamp...')

    date_time = [datetime.fromtimestamp(timestamp_).strftime('%Y/%m/%d %H:%M:%S')
                 for timestamp_ in timestamp]

    print('\t\tConverting datetime to timestamp...Done')
    return date_time
