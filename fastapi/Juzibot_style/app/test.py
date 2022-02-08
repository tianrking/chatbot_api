import matplotlib.pyplot as plt
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow.python.profiler import trace
import numpy as np
import cv2 

content_image_path = "/storage/lol/test/fastapi/Juzibot_style/gg.png"
style_image_path = "/storage/lol/test/fastapi/Juzibot_style/WallpaperDog20341285.png"
# Load content and style images (see example in the attached colab).
content_image = cv2.imread(content_image_path)
style_image = cv2.imread(style_image_path)
# Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
# Optionally resize the images. It is recommended that the style image is about
# 256 pixels (this size was used when training the style transfer network).
# The content image can be any size.
style_image = tf.image.resize(style_image, (256, 256))

# Load image stylization module.
hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Stylize image.
outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
stylized_image = outputs[0]