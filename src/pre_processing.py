import pandas as pd
import numpy as np
import mne


def load_annotations(file):
    # Load annotations file
    annotations = pd.read_csv(file, sep='\t', skiprows=21)
    # Create a DataFrame and remove the column named 'Position' because it is irrelevant.
    annotations_df = pd.DataFrame(data=annotations).drop(columns=['Position'], axis=1)

    return annotations_df


def load_signals(file):
    # Change sampling frequency from 512Hz to 128Hz -> 512/4 = 128
    # skip_rows = [row for row in range(107520, 177105) if row % 4 != 0]

    # Load signals file
    signals = pd.read_csv(file, sep='\t')  #, skiprows=skip_rows)
    signals_df = pd.DataFrame(data=signals)

    band_pass_filtering(signals_df)

    return signals_df


def band_pass_filtering(signals):
    # Apply band-pass filter
    signals_df = np.array([signals['F2-F4[uV]'], signals['F4-C4[uV]'], signals['F1-F3[uV]']])

    # Create a list with the channel names
    channel_names = ['F2-F4[uV]', 'F4-C4[uV]', 'F1-F3[uV]']
    # Channel types are all EEG
    channel_types = ['eeg', 'eeg', 'eeg']
    # Sampling rate
    sampling_frequency = 128  # Hz

    # Create the info-structure needed for our object with MNE
    info_structure = mne.create_info(ch_names=channel_names, sfreq=sampling_frequency, ch_types=channel_types)

    # Create raw object
    raw = mne.io.RawArray(signals_df, info_structure)

    # Band-pass filter, it takes frequencies from 0.05 - 30Hz.
    raw.filter(0.05, 30)
