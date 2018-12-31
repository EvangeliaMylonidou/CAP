from src.pre_processing import *


def main():
    # Load signals
    signal_file = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\signals\\n1.csv'
    signals = load_signals(file=signal_file)
    # print(signals)

    print('----------------------------------------------------------------------')

    # Load annotations
    annotation_file = 'D:\\liamylo\\Documents\\BSc Thesis\\CAP project\\data\\annotations\\n1.txt'
    annotations = load_annotations(file=annotation_file)
    # print(annotations)


if __name__ == "__main__":
    main()
