# from datetime import datetime

import pandas as pd


# Load signals data file
def load_signals():
    """
    signal_data_frame=pd.read_csv('n1.csv',sep=';')
    # Change sampling frequency from 512Hz to 105Hz

    skip_idx = [x for x in range(len(signal_data_frame)) if x % 5 != 0 or x<=107520 and x>0  or x>=17710592]
    signal_data_frame = pd.read_csv('n1.csv', skiprows=skip_idx, sep=';')


    signal_data_frame.to_csv('new_data')
    """
    signal_data_frame = pd.read_csv('new_data.csv', sep=',')

    test = pd.read_csv('new_data.csv', sep=',')
    print(test.columns)
    test1 = test.drop(['Unnamed: 0', 'Date', 'HH', 'MM', 'SS'], axis=1)
    test1.to_csv('test.txt', index=None, header=None)

    print(signal_data_frame.columns)
# ======================================================================================================================


# Load annotation file
def load_annotations():
    data = pd.read_csv('n1.txt', header=None)

    k = 0
    for i in range(0, 30):
        if repr(data[0][i]).split('\\') == ["'Sleep Stage", 'tPosition', 'tTime [hh:mm:ss]',
                                            'tEvent', 'tDuration[s]', "tLocation'"]:
            k = i
    print(k)

    annotations_data_frame = pd.DataFrame(
        columns=("'Sleep Stage", 'tTime [hh:mm:ss]', 'tEvent', 'tDuration[s]', "tLocation'"))

    L = []
    for i in annotations_data_frame.columns:
        for j in range(k + 1, len(data)):
            L.append(repr(data[0][j]).split('\\')[list(annotations_data_frame.columns).index(i)])

            annotations_data_frame[i] = L
        L = []

    a = list(df['Scoring'])

    print(a[33800:34100])

    for i in range(len(a)):
        print(i, a[i])

    print(annotations_data_frame.columns[-1])
# ======================================================================================================================


# times is the A-phases extracted from annotation file
def find_a_phases(annotations_data_frame, signal_data_frame):
    """
    times=[]
    for i in range(len(annotations_data_frame)):
        if annotations_data_frame['tDuration[s]'][i][-2]=='A':
            times.append(annotations_data_frame['tEvent'][i][1:])

     times[0]
    # ==================================================================================================================

     t=[]
     for i in range(len(annotations_data_frame['tDuration[s]'])):
        t.append(datetime.strptime((annotations_data_frame['tEvent'][i][1:]), '%H:%M:%S'))

    annotations_data_frame['time']=t
    """
    t = []
    for i in range(len(annotations_data_frame['tDuration[s]'])):
        t.append((annotations_data_frame['tEvent'][i][1:]))

    annotations_data_frame['time'] = t

    ss = []
    j = 0
    for i in range(len(signal_data_frame['SS'])):

        if str(signal_data_frame['SS'][i])[1] == '.':
            ss.append('0' + str(signal_data_frame['SS'][i])[0])
        else:
            ss.append(str(signal_data_frame['SS'][i])[0:2])
        j = j + 1
        print(j)

    signal_data_frame['SS'] = ss
    '''
    signal_data_frame.drop('SS', axis=1)
    
    signal_data_frame['SS'].to_csv('SS',index=False)
    
    signal_data_frame['SS'] = pd.read_csv('SS.csv')
    '''
    signal_data_frame['time'] = signal_data_frame['HH'].apply(str) + ":" + \
                                signal_data_frame['MM'].apply(str) + \
                                signal_data_frame['SS'].apply(str)

    new_time = []
    for i in range(len(signal_data_frame['time'])):
        print(i)
        if signal_data_frame['time'][i][1] == ':' and signal_data_frame['time'][i][3] == ':':
            new_time.append("0" + signal_data_frame['time'][i][0:2] + "0" + signal_data_frame['time'][i][2:])
        elif signal_data_frame['time'][i][1] == ':':
            new_time.append("0" + signal_data_frame['time'][i])
        elif signal_data_frame['time'][i][4] == ':':
            new_time.append(signal_data_frame['time'][i][0:3] + "0" + signal_data_frame['time'][i][3:])
        else:
            new_time.append(signal_data_frame['time'][i])

    signal_data_frame['time'] = new_time

    '''
    g = 0
    for i in signal_data_frame['time']:
        g = g + 1
        if g % 1000 == 0:
            print(g)
        signal_data_frame['time'] = datetime.strptime(i, '%H:%M:%S')

    # Convert time to timestamp

    A_phases_time = []



    for i in times:
        A_phases_time.append(datetime.strptime(i, '%H:%M:%S'))
    
    A = []
    for i in signal_data_frame['time']:
        A.append(i)
    
    for i in range(len(signal_data_frame['time'])):
        signal_data_frame['Scoring']
    
    signal_data_frame = signal_data_frame.drop('Scoring', axis=1)
    
    j = 0
    an = []
    data['Scoring'] = pd.Series()
    
    for i in range(1, len(annotations_data_frame)):
        print('i', i)
        while annotations_data_frame['time'][i - 1] <= signal_data_frame['time'][j] < annotations_data_frame['time'][i]:
            print(annotations_data_frame['time'][i - 1], j)
            an.append(annotations_data_frame['tDuration[s]'][i - 1][-2:])
            print(annotations_data_frame['tDuration[s]'][i - 1][-2:])
            j = j + 1
    
        while signal_data_frame['time'][j] >= annotations_data_frame['time'][i - 1]
    
    data['Scoring'] = pd.Series()
    
    an = []
    i = 1
    for j in range(len(signal_data_frame['time'])):
    
        while annotations_data_frame['time'][i] <= signal_data_frame['time'][j] < annotations_data_frame['time'][i + 1]:
            an.append(annotations_data_frame['tDuration[s]'][i - 1][-2:])
    
        i = i + 1
    
    for i in an:
        print(i)
    
    for i in signal_data_frame['Scoring']:
        if i != 'A1':
            print(i)
    '''
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
