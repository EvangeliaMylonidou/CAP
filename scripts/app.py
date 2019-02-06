from scripts.pre_processing.annotation_pre_processing import load_annotations
from scripts.pre_processing.signal_pre_processing import load_signals
from scripts.pre_processing.dataset_pre_processing import load_data_set
from scripts.plots import *
from scripts.model import *

from datetime import datetime

# ========== HOME ==========
ANNOTATIONS_TXT = 'D:\\liamylo\\Documents\\BSc Thesis\\Data\\Annotations\\n1.txt'
SIGNALS_CSV = 'D:\\liamylo\\Documents\\BSc Thesis\\Data\\Signals\\n1_512Hz.csv'
# ========== WORK ==========
# ANNOTATIONS_TXT = 'C:\\Users\\emylonidou\\PycharmProjects\\CAP\\data\\n1.txt'
# SIGNALS_CSV = 'C:\\Users\\emylonidou\\PycharmProjects\\CAP\\data\\n1_512Hz.csv'


def main():
    # ============================== PRE-PROCESSING ==============================
    print('============================ ANNOTATIONS =============================')
    annotations = load_annotations(file_name=ANNOTATIONS_TXT)
    # plot(annotations)

    print('============================== SIGNALS ===============================')
    signals = load_signals(file_name=SIGNALS_CSV)

    #

    #

    #

    #

    #

    #

    #

    print('============================= DATA-SET ===============================')
    data_set = load_data_set(signals=signals,
                             annotations=annotations[['Datetime', 'Event', 'Duration[s]']])
    # plot_data_classes(data_set)
    # save_data_set(data_set)

    # ================================== MODEL ===================================
    print('============================== MODEL =================================')

    print('============================= FINISHED ===============================')


if __name__ == "__main__":
    start_time = datetime.now()
    main()
    print(datetime.now() - start_time)
