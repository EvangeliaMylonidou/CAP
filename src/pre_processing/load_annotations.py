import pandas as pd


def load_annotations():
    # Load annotation file
    annotations = pd.read_csv('data/PhysioNet - The CAP Database/n1.txt', header=None)

    k = 0

    for i in range(0, 30):
        if repr(annotations[0][i]).split('\\') == ['Sleep Stage', 'tPosition', 'tTime [hh:mm:ss]',
                                                   'tEvent', 'tDuration[s]', 'tLocation']:
            k = i

    print('k = ', k)

    data_frame_annotations = pd.DataFrame(
        columns=('Sleep Stage', 'tTime [hh:mm:ss]', 'tEvent', 'tDuration[s]', 'tLocation')
    )

    L = []

    for i in data_frame_annotations.columns:
        for j in range(k + 1, len(annotations)):
            L.append(repr(annotations[0][j]).split('\\')[list(data_frame_annotations.columns).index(i)])

        data_frame_annotations[i] = L
        L = []

    print('data_frame_annotations = ', data_frame_annotations)
