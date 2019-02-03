import pandas as pd

from scripts.pre_processing.annotation_time_structure import create_datetime_structure

ANNOTATION_COLUMNS = ['Sleep Stage', 'Time [hh:mm:ss]', 'Event', 'Duration[s]']


def load_annotations(file_name):
    print('Loading annotations... ')
    # Load the signals from a file and save them into a DataFrame.
    annotations = _load_annotations(file_name)

    annotations = _create_datetime_structure(file_name, annotations)

    print('Loading annotations...Done')
    return annotations


def _load_annotations(file_name):
    print('\tLoad annotations file...')

    # Load the annotations from a file and save them into a DataFrame
    # Remove the column named 'Position' because it is irrelevant.
    annotations = pd.read_csv(file_name, sep='\t', skiprows=21, usecols=ANNOTATION_COLUMNS)

    print('\tLoad annotations file...Done')

    return annotations


def _create_datetime_structure(file_name, annotations):
    return create_datetime_structure(file_name, annotations)
