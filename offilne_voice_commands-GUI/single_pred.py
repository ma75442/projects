import pickle
import os
import numpy as np
from tqdm import tqdm
from scipy.io import wavfile
from python_speech_features import mfcc
from keras.models import load_model
import pandas as pd
from sklearn.metrics import accuracy_score
import librosa
import matplotlib.pyplot as plt
import clean as cl
#FOR PREDICTING GIVEN INPUT

def sip():
	with open('pickles/data.pickle', 'rb') as handle:
		config = pickle.load(handle)

	cl.clean()
	df = pd.read_csv('commands.csv')
	classes = list(np.unique(df.label))
	fn2class = dict(zip(df.fname, df.label))

	model = load_model(config.model_path)

	print('Extracting features from audio')
	rate, wav = wavfile.read('cleanAudio/output.wav')

	y_prob = []
	y_pred = []

	for i in range(0, wav.shape[0]-config.step, config.step):
		sample = wav[i:i+config.step]
		x = mfcc(sample, rate, numcep=config.nfeat, nfilt=config.nfilt, nfft=config.nfft)
		x = (x - config.min) / (config.max - config.min)

		if config.mode == 'conv':
			x = x.reshape(1, x.shape[0], x.shape[1], 1)
		elif config.mode == 'time':
			x = np.expand_dims(x, axis=0)
		y_hat = model.predict(x)
		y_prob.append(y_hat)
		y_pred.append(np.argmax(y_hat))

	fn_prob = np.mean(y_prob, axis=0).flatten()

	final_pred = classes[np.argmax(fn_prob)]

	return final_pred

