from mne.io import read_raw_edf
import pandas as pd


def to_data_frame(edf):
    """
    Converts an EDF file to DataFrame
    :param edf: The EDF file that needs to be converted into a DataFrame
    :return: Converted DataFrame
    """
    return read_raw_edf(edf).to_data_frame()


def to_csv(data_frame, csv):
    """
    Converts a DataFrame to CSV file format
    :param data_frame: The DataFrame that needs to be converted into CSV
    :param csv: The title of the CSV file that will be created
    :return: Converted CSV file
    """
    pd.DataFrame(data_frame).to_csv(csv)


def print_csv(csv):
    """
    Read and print in the console the whole csv file
    :param csv:
    """
    print(pd.read_csv(csv))


if __name__ == "__main__":
    edf_file = 'data/PhysioNet - The CAP Database/brux1.edf'
    csv_output_file = 'data/PhysioNet - The CAP Database/brux1_output.csv'

    to_csv(data_frame=to_data_frame(edf_file), csv=csv_output_file)
    print_csv(csv=csv_output_file)

    # load_signals_and_annotations()
