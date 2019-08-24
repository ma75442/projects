import os
import shutil
import random
import string
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Conv2D, MaxPool2D, Flatten, LSTM
from keras.layers import Dropout, Dense, TimeDistributed
from keras.models import Sequential, load_model
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint
from sklearn.utils.class_weight import compute_class_weight
from tqdm import tqdm
from python_speech_features import mfcc
import pickle

def aNd(c):
	with open('pickles/data.pickle', 'rb') as handle:
		config = pickle.load(handle)

	com_dict = {1:'abort',2:'activate',3:'centroid',4:'edge',5:'launch',6:'switch',7:'track',8:'zoom'}
	label = com_dict[int(c)]

	rate, signal = wavfile.read('cleanAudio/output.wav')

	n_samples = 2 * int((signal.shape[0]/rate)/0.1)

	classes = ['abort', 'activate', 'centroid', 'edge', 'launch', 'switch', 'track', 'zoom']

	def build_rand_feat():
		X = []
		y = []
		_min, _max = float('inf'), -float('inf')
		for _ in tqdm(range(n_samples)):
			rand_index = np.random.randint(0, signal.shape[0]-config.step)
			sample = signal[rand_index:rand_index+config.step]
			X_sample = mfcc(sample, rate, numcep=config.nfeat, nfilt=config.nfilt, nfft=config.nfft)
			_min = min(np.amin(X_sample), _min)
			_max = max(np.amax(X_sample), _max)
			X.append(X_sample)
			y.append(classes.index(label))
		X, y = np.array(X), np.array(y)
		X = (X - _min) / (_max - _min) 								#For normalisation
		if config.mode == 'conv':
			X = X.reshape(X.shape[0], X.shape[1], X.shape[2], 1)
		elif config.mode == 'mode':
			X = X.reshape(X.shape[0], X.shape[1], X.shape[2])
		y = to_categorical(y, num_classes=8)

		return X, y

	X, y = build_rand_feat()

	y_flat = np.argmax(y, axis=1)

	model = load_model(config.model_path)

	class_weight = compute_class_weight('balanced', np.unique(y_flat), y_flat)

	checkpoint = ModelCheckpoint(config.model_path, monitor='val_acc', verbose=1, mode='max', save_best_only=True, save_weights_only=False, period=1)

	model.fit(X, y, epochs=10,  batch_size=32, shuffle=True, class_weight=class_weight, validation_split=0.1, callbacks=[checkpoint])

	model.save(config.model_path)

	x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
	shutil.move('audioOutput/output.wav','commands/'+x+'.wav')

	df = pd.read_csv('commands.csv')
	df = df.append({'fname':x+'.wav','label':label},ignore_index=True)
	df.to_csv('commands.csv',index=False)

	return None