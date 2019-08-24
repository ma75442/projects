import os
import librosa
import pandas as pd
import numpy as np
from scipy.io import wavfile

def clean():
	def envelope(y, rate, threshold):
	    mask = []
	    y = pd.Series(y).apply(np.abs)
	    y_mean = y.rolling(window=int(rate/10), min_periods=1, center=True).mean()
	    for mean in y_mean:
	        if mean > threshold:
	            mask.append(True)
	        else:
	            mask.append(False)
	    return mask

	signal, rate = librosa.load('audioOutput/output.wav', sr=16000)
	mask = envelope(signal, rate, 0.0008)
	wavfile.write(filename='cleanAudio/output.wav', rate=rate, data=signal[mask])
	print('Audio cleaned.')