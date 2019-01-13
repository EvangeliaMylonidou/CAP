import pandas as pd


def find_a_phases(annotations_data_frame, signal_data_frame):

    j = 0
    an = []
    for i in range(1, len(annotations_data_frame['time'])):
        while signal_data_frame['time'][j] != annotations_data_frame['time'][i]:
            an.append(annotations_data_frame['tDuration[s]'][i - 1][-2:])
        j = j + 1
        print(j, ' ', i, ' ', annotations_data_frame['tDuration[s]'][i - 1][-2:])
        an.append(annotations_data_frame['tDuration[s]'][i][-2:])
        j = j + 1

    signal_data_frame['Scoring'] = an
    d1 = an

    d1 = pd.read_csv('d1', sep=',', header=None)
    signal_data_frame['Scoring'] = d1
    signal_data_frame['Scoring'].to_csv('d1', index=False)

    signal_data_frame.to_csv('whole dataset', index=False)
    signal_data_frame = signal_data_frame.drop(['Unnamed: 0', 'HH', 'MM', 'SS'], axis=1)
    # Rearrange columns
    signal_data_frame = signal_data_frame[['Date', 'time', 'F4-C4[uV]', 'F3-C3[uV]', 'Scoring']]

    signal_data_frame.to_csv('final', index=False)
    test = pd.read_csv('final', sep=',')

    signal_data_frame = signal_data_frame.drop(['Date', 'time', 'Scoring'], axis=1)
    signal_data_frame.to_csv('Professor', index=False, header=None)

    list(signal_data_frame['time']).index('07:34:13')

    for i in range(3000000):
        print(signal_data_frame['time'][i], signal_data_frame['Scoring'][i])

    # sampling frequency must be 119

    d1 = pd.read_csv('whole dataset', sep=',', usecols=['Scoring'])

    d1 = d1.drop(['Date', 'time'], axis=1)
    d1.to_csv('test3.csv', index=False, header=None)

    print(d1.columns)
