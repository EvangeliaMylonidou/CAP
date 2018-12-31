import matplotlib.pyplot as plt
import numpy as np


def plot_annotations(annotations):

    # Plot attributes
    number_of_patterns, number_of_attributes = np.shape(annotations)
    print(np.shape(annotations))

    plt.figure(1)
    plt.title('Annotation plotting')
    for p in range(number_of_patterns):
        if annotations[p,3] == 'MCAP-A1':
            plt.plot(annotations, '.', color='red')
        elif annotations['Event'] == 'MCAP-A2':
            plt.plot(annotations, '.', color='green')
        elif annotations['Event'] == 'MCAP-A3':
            plt.plot(annotations, '.', color='blue')
        else:
            plt.plot(annotations, '.', color='yellow')
