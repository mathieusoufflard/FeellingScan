import os
import cv2
import tensorflow as tf
import numpy

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

model = tf.keras.models.load_model('feel_ia.h5')


CATEGORIES = ["Angry", "Happy", "Sad", "Tired"]
test_batches = "uploads/capture.jpg"


def prepare(filepath):
    SIZE = 224  # 50 in txt-based
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (SIZE, SIZE))
    return new_array.reshape(-1, SIZE, SIZE, 3)

def main():
    predictions = model.predict([prepare(test_batches)])
    result = numpy.where(predictions[0] == numpy.amax(predictions[0]))
    print(CATEGORIES[result[0][0]])
    return CATEGORIES[result[0][0]]
