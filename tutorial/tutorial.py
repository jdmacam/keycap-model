# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

# The Fashion MNIST dataset contains 70,000 grayscale images in 10 categories. 
# The images show individual articles of clothing at low resolution (28 by 28 pixels),
# as seen here  https://tensorflow.org/images/fashion-mnist-sprite.png
fashion_mnist = tf.keras.datasets.fashion_mnist

# Here, 60,000 images are used to train the network and 10,000 images to evaluate how accurately 
# the network learned to classify images.
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# list to convert the int labels to their clothing representation
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# print the format of the dataset in the format (<number of images>, <x-resolution pixels>, <y-resolution pixels>)
print(train_images.shape)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()