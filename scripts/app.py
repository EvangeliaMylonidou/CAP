from scripts.pre_processing.annotation_pre_processing import load_annotations
from scripts.pre_processing.signal_pre_processing import load_signals
from scripts.pre_processing.dataset_pre_processing import create_data_set
from datetime import datetime

import pandas as pd


annotations_txt = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\annotations\\n1.txt'
signals_csv = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\n1_512Hz.csv'
modified_signals_csv = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\n1_signals_pre_processed.csv'
modified_annotations_txt = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP ' \
                           'project\\data\\signals\\n1_annotations_pre_processed.txt'
data_set_csv = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\data_set.csv'


def main():
    start_time = datetime.now()
    # ============================== PRE-PROCESSING ==============================
    print('============================ ANNOTATIONS =============================')
    annotations = load_annotations(file_name=annotations_txt)

    print('============================== SIGNALS ===============================')
    signals = load_signals(file_name=signals_csv)

    print('============================= DATA-SET ===============================')
    data_set = create_data_set(signals=signals[['Datetime', 'F2-F4[uV]', 'F4-C4[uV]', 'F1-F3[uV]']],
                               annotations=annotations[['Datetime', 'Sleep Stage', 'Event', 'Duration[s]']])
    print(data_set)
    save_data_set(data_set)

    print(datetime.now() - start_time)

    # ================================== MODEL ===================================
    print('============================= FINISHED ===============================')


def load_signals_second_time():
    return pd.read_csv(modified_signals_csv, sep=',', index_col=0, nrows=10000)


def load_annotations_second_time():
    return pd.read_csv(modified_annotations_txt, sep=',', index_col=0)


def save_signals(signals):
    signals.to_csv(modified_signals_csv, index=False)


def save_annotations(annotations):
    annotations.to_csv(modified_annotations_txt, index=False)


def save_data_set(data_set):
    data_set.to_csv(data_set_csv, index=False)


if __name__ == "__main__":
    main()
