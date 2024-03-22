import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file()
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

text = text[300000:800000]

characters = sorted(set(text))

char_to_index = dict((c,i) for i,c in enumerate(characters))
index_to_char = dict((i,c) for i,c in enumerate(characters))

sequence_length = 40
steps = 3

sentences = []
next_characters = []

for i in range(0, len(text)-sequence_length,steps):
    sentences.append(text[i : i+sequence_length])
    next_characters.append(text[i+sequence_length])