from datetime import datetime
import pandas as pd
import re


# ============================ ANNOTATIONS ============================

def create_datetime_structure(file_name, annotations):
    print('\tCreate annotation datetime structure...')

    # Extract annotation start and end of recording dates.
    recording_dates = _get_recording_dates(file_name)

    # Combine the recording dates with the Time [hh:mm:ss] in one column named Datetime.
    date_time = _concatenate_date_and_time(annotations['Time [hh:mm:ss]'], recording_dates)

    # Insert column Datetime in the first column of the DataFrame
    annotations.insert(loc=0, column='Datetime', value=date_time)

    # Delete column 'Time [hh:mm:ss]' because it is no longer needed,
    # and is replaced by the column: Datetime
    annotations.drop(columns=['Time [hh:mm:ss]'], axis=1, inplace=True)

    print('\tCreate annotation datetime structure...Done')
    return annotations


def _get_recording_dates(file_name):
    print('\t\tGet annotation recording dates...')
    annotations = pd.read_csv(file_name, sep='/t', nrows=20, engine='python')

    match_start = re.search(r'\d{2}/\d{2}/\d{4}', str(annotations.iloc[2].values))
    match_end = re.search(r'\d{2}/\d{2}/\d{4}', str(annotations.iloc[-1].values))

    start_date = datetime.strptime(match_start.group(), '%d/%m/%Y').strftime('%Y/%m/%d')
    end_date = datetime.strptime(match_end.group(), '%d/%m/%Y').strftime('%Y/%m/%d')

    print('\t\tGet annotation recording dates...Done')

    return {'start_date': start_date, 'end_date': end_date}


def _concatenate_date_and_time(annotations_time, recording_dates):
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



