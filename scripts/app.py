from scripts.pre_processing.annotation_pre_processing import load_annotations
from scripts.pre_processing.signal_pre_processing import load_signals
from scripts.pre_processing.dataset_pre_processing import load_data_set

from datetime import datetime


ANNOTATIONS_TXT = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\annotations\\n1.txt'
SIGNALS_CSV = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\n1_512Hz.csv'
SIGNALS_EDF = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\edf\\n1.edf'


def main():
    # ============================== PRE-PROCESSING ==============================
    print('============================ ANNOTATIONS =============================')
    annotations = load_annotations(file_name=ANNOTATIONS_TXT)

    print('============================== SIGNALS ===============================')
    signals = load_signals(file_name=SIGNALS_CSV)

    print('============================= DATA-SET ===============================')
    data_set = load_data_set(signals=signals,
                             annotations=annotations[['Datetime', 'Sleep Stage', 'Event', 'Duration[s]']])
    print(data_set)
    # save_data_set(data_set)

    # ================================== MODEL ===================================
    print('============================= FINISHED ===============================')


if __name__ == "__main__":
    start_time = datetime.now()
    main()
    print(datetime.now() - start_time)
