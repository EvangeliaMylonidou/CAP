import pandas as pd
# import time
# import datetime
# from datetime import datetime, date, time,timedelta
# from scipy.signal import butter, lfilter
import numpy as np
import mne

# dfdata=pd.read_csv('new_data.csv', sep=',', nrows=1000)

# Load signals data file

# dfdata=pd.read_csv('n1.csv',sep=';')

# Change sampling frequency from 512Hz to 105Hz
# pairnei ana 5 grammes 512/5 = 102.4 ana deuterolepto gia 100Hz - resampling
# skip_idx = [x for x in range(107520, 17710592) if x % 5 != 0]
# dfdata = pd.read_csv('n1.csv', skiprows=skip_idx, sep=';')
#
#
# dfdata.to_csv('new_data')

dfdata = pd.read_csv('new_data.csv', sep=',', nrows=1000)

# dfdata.to_csv('new_data1')

# Apply band pass filter

df = dfdata[['F4-C4[uV]', 'C4-P4[uV]', 'F3-C3[uV]', 'C3-P3[uV]']]
# antikatastash tou koma me teleia epeidh to dekadiko to xwrize me teleies
for i in df.columns:
    for j in range(len(df['F4-C4[uV]'])):
        #        df[i][j].replace(',','.')
        df[i][j] = float(df[i][j].replace(',', '.'))
        print(j)

data = np.array([df['F4-C4[uV]'], df['C4-P4[uV]'], df['F3-C3[uV]'], df['C3-P3[uV]']])
# channel names lista me onomata
ch_names = ['F4-C4[uV]', 'C4-P4[uV]', 'F3-C3[uV]', 'C3-P3[uV]']

# Sampling rate
sfreq = 115  # Hz frequency
ch_types = ['eeg', 'eeg', 'eeg', 'eeg']  # channelttypes = eeg
# Create the info structure needed by MNE plhrofories gia to antikeimeno pou 8eloume na dhmiourghsoyme
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

# Finally, create the Raw object
raw = mne.io.RawArray(data, info)
# band pass filter pernane oi suxnothtes apo 0.05 mexri 30
raw.filter(0.05, 30, fir_design='firwin')
