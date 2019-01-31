import matplotlib.pyplot as plt
import mne
import numpy as np


def plot_amount_of_cap(annotations):
    print('Plotting CAP...')

    number_of_patterns, number_of_attributes = np.shape(annotations)
    count_a1 = count_a2 = count_a3 = 0

    for p in range(number_of_patterns):
        # ----------- CAP -----------
        print(annotations['Event'][p])
        if annotations['Event'][p] == 'MCAP-A1':
            count_a1 += 1
            break
        elif annotations['Event'][p] == 'MCAP-A2':
            count_a2 += 1
            break
        elif annotations['Event'][p] == 'MCAP-A3':
            count_a3 += 1
            break

    plt.plot(1, count_a1, '*', color='green')
    plt.plot(2, count_a2, '*', color='yellow')
    plt.plot(3, count_a3, '*', color='orange')
    plt.show()


def plot_amount_of_annotations(annotations):
    print('Plotting annotations...')

    number_of_patterns, number_of_attributes = np.shape(annotations)
    count_a1 = count_a2 = count_a3 =  \
        count_s0 = count_s1 = count_s2 = count_s3 = \
        count_s4 = count_srem = count_unscored = 0

    for p in range(number_of_patterns):
        # ----------- CAP -----------
        print(annotations['Event'][p])
        if annotations['Event'][p] == 'MCAP-A1':
            count_a1 += 1
            break
        elif annotations['Event'][p] == 'MCAP-A2':
            count_a2 += 1
            break
        elif annotations['Event'][p] == 'MCAP-A3':
            count_a3 += 1
            break
        # ---------- SLEEP ----------
        elif annotations['Event'][p] == 'SLEEP-S0':
            count_s0 += 1
            break
        elif annotations['Event'][p] == 'SLEEP-S1':
            count_s1 += 1
            break
        elif annotations['Event'][p] == 'SLEEP-S2':
            count_s2 += 1
            break
        elif annotations['Event'][p] == 'SLEEP-S3':
            count_s3 += 1
            break
        elif annotations['Event'][p] == 'SLEEP-S4':
            count_s4 += 1
            break
        elif annotations['Event'][p] == 'SLEEP-REM':
            count_srem += 1
            break
        else:
            count_unscored += 1
            break

    # ----------- CAP -----------
    plt.title('Annotation plotting')
    plt.plot(1, count_a1, '*', color='green')
    plt.plot(2, count_a2, '*', color='yellow')
    plt.plot(3, count_a3, '*', color='orange')
    # ---------- SLEEP ----------
    plt.plot(4, count_s0, '*', color='red')
    plt.plot(5, count_s1, '*', color='pink')
    plt.plot(6, count_s2, '*', color='maroon')
    plt.plot(7, count_s3, '*', color='purple')
    plt.plot(8, count_s4, '*', color='blue')
    plt.plot(9, count_srem, '*', color='navy')
    plt.plot(10, count_unscored, '*', color='black')
    plt.show()


def plot_re_sampled_signals(epochs, epochs_re_sampled):
    # Plot a piece of data to see the effects of down-sampling
    plt.figure(figsize=(7, 3))

    n_samples_to_plot = int(0.5 * epochs.info['sfreq'])  # plot 0.5 seconds of data
    plt.plot(epochs.times[:n_samples_to_plot],
             epochs.get_data()[0, 0, :n_samples_to_plot], color='black')

    n_samples_to_plot = int(0.5 * epochs_re_sampled.info['sfreq'])
    plt.plot(epochs_re_sampled.times[:n_samples_to_plot],
             epochs_re_sampled.get_data()[0, 0, :n_samples_to_plot],
             '-o', color='red')

    plt.xlabel('time (s)')
    plt.legend(['original', 'down-sampled'], loc='best')
    plt.title('Effect of down-sampling')
    mne.viz.tight_layout()
