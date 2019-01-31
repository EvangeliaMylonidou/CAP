import pandas as pd
import numpy as np

from datetime import datetime
from scipy import signal
from window_slider import Slider


def load_data_set(signals, annotations):
    print('Loading data-set...')
    data_set = _create_data_set(signals=signals, annotations=annotations)
    data_set = _fill_data_set(data_set)

    data_set = _re_sampling(data_set)
    print(data_set)

    _windowing(data_set)
    # print(data_set)

    print('Loading data-set...Done')
    return data_set


def _create_data_set(signals, annotations):
    print('Creating data-set...')

    signals['Datetime'] = pd.to_datetime(signals.Datetime)
    annotations['Datetime'] = pd.to_datetime(annotations.Datetime)
    data_set = pd.merge_asof(left=signals, right=annotations, on='Datetime')

    print('Creating data-set...Done')
    return data_set


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


def _convert_datetime_to_timestamp(date_time):
    print('\t\tConverting datetime to timestamp...')

    timestamp = [datetime.strptime(datetime_, '%Y/%m/%d %H:%M:%S').timestamp() for datetime_ in date_time]

    print('\t\tConverting datetime to timestamp...Done')
    return timestamp


def _convert_timestamp_to_datetime(timestamp):
    print('\t\tConverting datetime to timestamp...')

    date_time = [datetime.utcfromtimestamp(timestamp_).strftime('%Y/%m/%d %H:%M:%S')
                 for timestamp_ in timestamp]

    print('\t\tConverting datetime to timestamp...Done')
    return date_time


def _re_sampling(data_set):
    print('\tRe-sampling...')

    freq_100_hz = 512 / 100
    total_amount_of_signals = len(data_set) / freq_100_hz

    re_sampled_data = signal.resample(data_set, int(total_amount_of_signals))
    data_set = pd.DataFrame(re_sampled_data, columns=list(data_set))

    print('\tRe-sampling...Done')
    return data_set


def _windowing(data_set):
    print('\tWindowing...')

    bucket_size = 2
    overlap_count = 1

    slider = Slider(bucket_size, overlap_count)
    slider.fit(np.asarray(data_set))

    while True:
        window_data = slider.slide()
        if slider.reached_end_of_list():
            break

    print(data_set.head())
    signals = pd.DataFrame(window_data)
    print(signals.head())

    print('\tWindowing...Done')
