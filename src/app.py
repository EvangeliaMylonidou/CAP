from src.pre_processing import load_signals, load_annotations


def main():
    signal_file = ''
    annotation_file = ''

    signals = load_signals(file=signal_file)
    annotations = load_annotations(file=annotation_file)


if __name__ == "__main__":
    main()
