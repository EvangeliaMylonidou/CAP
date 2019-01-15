from datetime import datetime

import pandas as pd
import re


def load_annotations(file_name):
    print('Loading annotations... ')
    # Load the signals from a file and save them into a DataFrame.
    annotations = _load_annotations(file_name)

    annotations = _create_annotation_datetime_structure(file_name, annotations)

    print('Loading annotations...Done')
    return annotations


def _load_annotations(file_name):
    print('\tLoad annotations file...')

    # Load the annotations from a file and save them into a DataFrame
    # Remove the column named 'Position' because it is irrelevant.
    annotations = pd.read_csv(file_name, sep='\t', skiprows=21).drop(columns=['Position'], axis=1)
    print('\tLoad annotations file...Done')

    return annotations


def _create_annotation_datetime_structure(file_name, annotations):

    print('\tCreate annotation datetime structure...')

    # Extract annotation start and end of recording dates.
    recording_dates = _get_annotation_recording_dates(file_name)

    # Combine the recording dates with the Time [hh:mm:ss] in one column named Datetime.
    date_time = _concatenate_annotation_date_and_time(annotations['Time [hh:mm:ss]'], recording_dates)

    annotations.insert(loc=0, column='Datetime', value=date_time)
    annotations.drop(columns=['Time [hh:mm:ss]'], axis=1, inplace=True)

    print('\tCreate annotation datetime structure...Done')

    return annotations


def _get_annotation_recording_dates(file_name):
    print('\t\tGet annotation recording dates...')
    annotations = pd.read_csv(file_name, sep='/t', nrows=20, engine='python')

    match_start = re.search(r'\d{2}/\d{2}/\d{4}', str(annotations.iloc[2].values))
    match_end = re.search(r'\d{2}/\d{2}/\d{4}', str(annotations.iloc[-1].values))

    start_date = datetime.strptime(match_start.group(), '%d/%m/%Y').strftime('%Y/%m/%d')
    end_date = datetime.strptime(match_end.group(), '%d/%m/%Y').strftime('%Y/%m/%d')

    print('\t\tGet annotation recording dates...Done')

    return {'start_date': start_date, 'end_date': end_date}


def _concatenate_annotation_date_and_time(annotations_time, recording_dates):
    print('\t\tConcatenate annotations date and time...')
    date_time = []
    date = recording_dates['start_date']
    midnight = '00:00:00'

    for i in range(len(annotations_time)):
        if annotations_time[i].split(':')[0] == midnight.split(':')[0] and date != recording_dates['end_date']:
            date = recording_dates['end_date']

        date_time.append("{} {}".format(date, str(annotations_time[i])))

    print('\t\tConcatenate annotations date and time...Done')
    return date_time
