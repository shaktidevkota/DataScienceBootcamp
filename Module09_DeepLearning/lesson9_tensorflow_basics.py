#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense
f#rom tensorflow.keras.layers import Dropout
#from tensorflow.keras.optimizers import Adam
#from tensorflow.keras.callbacks import EarlyStopping
#from tensorflow.keras.models import load_model

import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

print("Available GPUs:", len(tf.config.list_physical_devices("GPU")))