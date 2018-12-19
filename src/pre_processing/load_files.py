import scipy.io


def load_matlab_file(file_name):
    """
    Loads a MATLAB code file.

    :param file_name: The name of the file or the path to the file :type: String
    :return:
    """
    data = scipy.io.loadmat(file_name)  # "feature_extraction.mat" /.mat
    print(data)
    print(data["y"])
    print(data["y"][1])


if __name__ == "__main__":
    load_matlab_file('feature_extraction.mat')
