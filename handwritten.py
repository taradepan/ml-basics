import cv2 
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnint.load_data()

x_train = tf.keras.utils.normalizes(x_train, axis=1)
x_test = tf.keras.utils.normalizes(x_test, axis=1)

model = tf.keras.models.sequential()
model.add(tf.keras.layers.flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(unit=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(unit=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(unit=10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metric=['accuracy'])

model.fit(x_train, y_train, epoch=3)

loss, accuracy = model.evaluate(x_test, y_test)
print(accuracy)
print(loss)

model.save('digits.model')