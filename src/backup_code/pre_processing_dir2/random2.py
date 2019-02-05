from datetime import datetime
import pandas as pd


# times is the A-phases extracted from annotation file
def find_a_phases(annotations, signals):
    times = []
    for i in range(len(annotations)):
        if annotations['Duration[s]'][i][-2] == 'A':
            times.append(annotations['Event'][i][1:])

    print('Times[0]')
    print(times[0])

    g = 0
    for i in signals['time']:
        g = g + 1
        if g % 1000 == 0:
            print(g)
        signals['time'] = datetime.strptime(i, '%H:%M:%S')

    # Convert time to timestamp

    a_phases_time = []

    for i in times:
        a_phases_time.append(datetime.strptime(i, '%H:%M:%S'))

    A = []
    for i in signals['time']:
        A.append(i)

    for i in range(len(signals['time'])):
        signals['Scoring']

    signals = signals.drop('Scoring', axis=1)

    j = 0
    an = []
    data = pd.DataFrame()
    data['Scoring'] = pd.Series()

    for i in range(1, len(annotations)):
        print('i', i)
        while annotations['time'][i - 1] <= signals['time'][j] < annotations['time'][i]:
            print(annotations['time'][i - 1], j)
            an.append(annotations['tDuration[s]'][i - 1][-2:])
            print(annotations['tDuration[s]'][i - 1][-2:])
            j = j + 1

        while signals['time'][j] >= annotations['time'][i - 1]:
            print('WTF is this doing here?')

    data['Scoring'] = pd.Series()

    an = []
    i = 1
    for j in range(len(signals['time'])):

        while annotations['time'][i] <= signals['time'][j] < annotations['time'][i + 1]:
            an.append(annotations['tDuration[s]'][i - 1][-2:])

        i = i + 1

    for i in an:
        print(i)

    for i in signals['Scoring']:
        if i != 'A1':
            print(i)
