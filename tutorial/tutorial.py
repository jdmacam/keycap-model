import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

print(tf.__version__)

import pathlib
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)

# .glob() returns an object of a list of files with the given syntax
# convert to a list to access that list
image_count = len(list(data_dir.glob("*/*.jpg")))

print (f"Number of images: {image_count}")


roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[0]))