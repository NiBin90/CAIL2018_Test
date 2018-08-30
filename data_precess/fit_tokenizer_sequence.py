import pickle
import jieba
import json
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

jieba.setLogLevel('WARN')

num_words = 80000
maxlen = 400

tokenizer_fact = Tokenizer(num_words=num_words)
print(tokenizer_fact)

with open('tokenizer_fact_%d.pkl' % (num_words), mode='rb') as f:
    tokenizer_fact=pickle.load(f)
