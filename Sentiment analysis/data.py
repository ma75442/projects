import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import PySimpleGUI as sg  


df= pd.read_csv('com_1review.csv')
print(df)
l=len(df)
col=df.mpos
print(l)
#Positive response
mpost=df['mpos'].sum()
mpost=mpost/l
gpost=df['gpos'].sum()
gpost=gpost/l
wpost=df['wpos'].sum()
wpost=wpost/l
vpost=df['vpos'].sum()
vpost=vpost/l
jpost=df['jpos'].sum()
jpost=jpost/l
fpost=df['fpos'].sum()
fpost=fpost/l