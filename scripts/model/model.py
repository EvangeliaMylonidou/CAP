import sklearn.model_selection as sk
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense
from keras.activations import softmax


def cross_validation(X, t, folds=10):
    print('{}-fold Cross-Validation...'.format(folds))

    for fold in range(folds):
        # Split train and test sets...
        X_train, X_test, t_train, t_test = sk.train_test_split(X, t, test_size=0.1)

    print('{}-fold Cross-Validation...Done'.format(folds))
    return X_train, X_test, t_train, t_test


def cnn1D():
    model = Sequential(name='cnn1D')
    model.add(Conv1D(kernel_size=10, filters=32, kernel_initializer='he_normal', activation='relu'))
    print(model.output_shape)
    # Max Pooling : The maximum output in a rectangular neighbourhood. It is used to make the network more flexible
    # to slight changes and decrease the network computationl expenses by extracting the group of pixels that are
    # highly contributing to each feature in the feature maps in the layer.
    model.add(MaxPooling1D(pool_size=20, strides=10))
    # model.add(Dropout(0.2))
    print(model.output_shape)

    model.add(Conv1D(kernel_size=10, filters=32, kernel_initializer='he_normal', activation='relu'))
    print(model.output_shape)

    model.add(MaxPooling1D(pool_size=20, strides=10))
    # model.add(Dropout(0.2))
    print(model.output_shape)

    # The dense layer is a fully connected layer that comes after the convolutional layers
    # and they give us the output vector of the Network.
    model.add(Dense())
    model.add(softmax(x=1))
