import matplotlib.pyplot as plt
import tensorflow as tf

def preprocess(image_path='data/raw/gonzalez.tif'):
    input_image = plt.imread(fname=image_path, format="tif")
    input_image = tf.cast(input_image, tf.float32) / 255.0

