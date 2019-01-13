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
    # save_annotations(annotations)

    print('============================== SIGNALS ===============================')
    signals = load_signals(file_name=signals_csv)
    # save_signals(signals)

    print('============================= DATA-SET ===============================')
    create_data_set(annotations=annotations, signals=signals)

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


if __name__ == "__main__":
    main()
