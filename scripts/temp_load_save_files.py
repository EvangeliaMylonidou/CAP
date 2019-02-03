import pandas as pd

MODIFIED_SIGNALS_CSV = 'D:\\liamylo\\Documents\\BSc Thesis\\Data\\Pre-processed\\n1_signals_pre_processed.csv'
MODIFIED_ANNOTATIONS_TXT = 'D:\\liamylo\\Documents\\BSc Thesis\\Data\\Pre-processed\\n1_annotations_pre_processed.txt '
DATA_SET_CSV = 'D:\\liamylo\\Documents\\BSc Thesis\\Data\\Pre-processed\\data_set.csv'


def load_signals_second_time():
    return pd.read_csv(MODIFIED_SIGNALS_CSV, sep=',', index_col=0, nrows=10000)


def load_annotations_second_time():
    return pd.read_csv(MODIFIED_ANNOTATIONS_TXT, sep=',', index_col=0)


def save_signals(signals):
    signals.to_csv(MODIFIED_SIGNALS_CSV, index=False)


def save_annotations(annotations):
    annotations.to_csv(MODIFIED_ANNOTATIONS_TXT, index=False)


def save_data_set(data_set):
    data_set.to_csv(DATA_SET_CSV, index=False)
