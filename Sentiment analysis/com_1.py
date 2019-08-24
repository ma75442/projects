import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

  
df= pd.read_csv('com_1review.csv')
print(df)
#rows=list(df)
l=len(df)

col=df.mpos
print(l)
#work  productivity  punctuality performance ethics nwork npro  npunct  nper  nethics presult nresult review  nreview preview
#company  manage  grow  work  vision  job flex  mpos  gpos  wpos  vpos  jpos  fpos  mneg  gneg  wneg  vneg  jneg  fneg

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

#plot
plt.subplot(2,2,1)
objects = ('Management', 'Growth', 'Work', 'Vision','job','Flexibility')
y_pos = np.arange(len(objects))
performance = [mpost,gpost,wpost,vpost,jpost,fpost]

plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.xlabel('Company Parameters')
plt.title('Positive response')

plt.subplot(2,2,2)
objects = ('Management', 'Growth', 'Work', 'Vision','job','Flexibility')
y_pos = np.arange(len(objects))
performance = [mnegt,gnegt,wnegt,vnegt,jnegt,fnegt]

plt.bar(y_pos, performance, align='center', alpha=0.7,color='green')
plt.xticks(y_pos, objects)
plt.xlabel('Company Parameters')
plt.title('Negative response')

plt.subplot(2,2,3)
labels = 'Positive', 'Negative'
sizes = [presultt, nresultt]
colors = ['cyan', 'red']
explode = (0.1, 0)  # explode 1st slice
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.show()



#previewt=df['preview'].sum()
#nreviewt=df['nreview'].sum()


'''with open('positive.csv','a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(p)
  csvfile.close()
'''