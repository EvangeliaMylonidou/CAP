import matplotlib.pyplot as plt


def plot(annotations):
    print('Plotting different phases...')

    target_count = annotations['Event'].value_counts()
    print(target_count)

    plt.title('Annotation Events')
    plt.xlabel('Event')
    plt.ylabel('Count')
    plt.plot(target_count)
    plt.show()

    print('Plotting different phases...Done')

