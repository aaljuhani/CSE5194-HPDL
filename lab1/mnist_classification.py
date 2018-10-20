# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from keras.datasets import cifar10

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

mnist_dataset = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist_dataset.load_data()
