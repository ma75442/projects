import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


df= pd.read_csv('com_2review.csv')
print(df)
#rows=list(df)
l=len(df)

col=df.mpos
print(l)
#work  productivity  punctuality performance ethics nwork npro  npunct  nper  nethics presult nresult review  nreview preview
#company  manage  grow  work  vision  job flex  mpos  gpos  wpos  vpos  jpos  fpos  mneg  gneg  wneg  vneg  jneg  fneg
i=0

i=df['manage'].search('yes')
print('ppp'+str(i)+'i')
#Positive response
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

#Negative response
mnegt=df['mneg'].sum()
mnegt=mnegt/l
gnegt=df['gneg'].sum()
gnegt=gnegt/l
wnegt=df['wneg'].sum()
wnegt=wnegt/l
vnegt=df['vneg'].sum()
vnegt=vnegt/l
jnegt=df['jneg'].sum()
jnegt=jnegt/l
fnegt=df['fneg'].sum()
fnegt=fnegt/l

#result

presultt=(mpost+gpost+wpost+vpost+jpost+fpost)*0.6  #3.6/6

nresultt=(mnegt+gnegt+wnegt+vnegt+jnegt+fnegt)*0.6
