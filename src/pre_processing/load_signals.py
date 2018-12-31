import pandas as pd
import numpy as np
import mne


def sampling():
    # Change sampling frequency from 512Hz to 105Hz
    """ It takes every 5 lines: 512/5 = 102.5 per second for 100Hz - re-sampling """
    skip_rows = [row for row in range(start=107520, stop=17710592) if row % 5 != 0]
    # Load signals from data file
    data_frame_data = pd.read_csv('n1.csv', skiprows=skip_rows, sep=';')

    # Save the new data into a csv file
    data_frame_data.to_csv('new_data')


def band_pass_filtering():
    # Load signals from data file
    data_frame_data = pd.read_csv('new_data.csv', sep=',', nrows=1000)

    # Apply band-pass filter
    data_frame = data_frame_data[['F4-C4[uV]', 'C4-P4[uV]', 'F3-C3[uv]', 'C3-P3[uv]']]

    # Replace all comas (,) with dots (.) because the decimal numbers are separated with dots.
    for i in data_frame.columns:
        for j in range(len(data_frame['F4-C4[uV]'])):
            data_frame[i][j] = float(data_frame[i][j].replace(',', '.'))
            print(j)

    data = np.array([data_frame['F4-C4[uV]'], data_frame['C4-P4[uV]'], data_frame['F3-C3[uV]'], data_frame['C3-P3[uV]']])

    # Channel_names is a list with names
    channel_names = ['F4-C4[uV]', 'C4-P4[uV]', 'F3-C3[uV]', 'C3-P3[uV]']

    # Sampling rate
    sampling_frequency = 115  # Hz
    channel_types = ['eeg', 'eeg', 'eeg', 'eeg']  # channel_types = eeg

    # Create the info structure needed with MNE
    # Here is the info for the object we want to create
    info = mne.create_info(ch_names=channel_names, sfreq=sampling_frequency, ch_types=channel_types)

    # Finally, create the raw object
    raw = mne.io.RawArray(data, info)

    # Band pass filter
    # It takes frequencies from 0.05 - 30Hz
    raw.filter(0.05, 30, fir_design='firwin')
