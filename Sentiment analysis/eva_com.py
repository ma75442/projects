import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def word_feats(words):
    return dict([(word, True) for word in words])
'''with open("positive.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header)
    posi = [r for r in reader]
#print(posi) '''
import PySimpleGUI as sg


sg.ChangeLookAndFeel('Dark')  
layout =[[sg.Text('Employee Satisfaction Survey', size=(29, 1), font=("Helvetica", 25))],
[sg.Text('Company:'),sg.OptionMenu(('Company_1','Company_2'), size=(20, 3),key='_coma_')],
[sg.Text('How satisfied are you with the following aspects of your job?')],
[sg.Text('Is the Management of the company well on track?  (exceptionally/absolutely/poor):'),sg.InputText(key='_manage_')],
[sg.Text('Are you satisfied with the Growth Opportunities? (yes/ no)                               :'),sg.InputText(key='_grow_')],
[sg.Text('How is the Work Culture here?(competitive/poor)                                            :'),sg.InputText(key='_work_')],
[sg.Text('Value and Vision (extraordinary/shortsighted)                                             :'),sg.InputText(key='_vision_')],
[sg.Text('Overall how much satisfied are you with your job? (extremely satisfied/no)      :'),sg.InputText(key='_job_')],
[sg.Text('Flexibility (outstanding/worse)                                                                  :'),sg.InputText(key='_flex_')],
[sg.Submit('upload',key='_OK BUTTON_'), sg.Cancel()],
[sg.Text('_'  * 80)],
[sg.Output(size=(140, 10))]] 

positive_vocab = ['yes','extraordinary', 'outstanding', 'absolutely', 'very strongly', 'appreciative', 'competitive', 'exceptionally','sustainable','extremely satisfied']
negative_vocab = ['unsatisfactory', 'mainstream','deteoriorating','avoid','shortsighted','low','vulnerable','somewhat', 'worse','unsatisfied','no','poor']
neutral_vocab = ['middling','fair','moderately satisfied','ordinary','average','mediocre']

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab] 
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]   
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)

# Predict
neg = 0
pos = 0 

   
window = sg.Window('Get filename example',default_element_size=(40,1)).Layout(layout)

# The Event Loop  
while True:  
  event, values = window.Read()  
  if event is None:  
        break  
  if event == '_OK BUTTON_':
    com=values['_coma_']
    manage=values['_manage_']
    grow=values['_grow_']
    work=values['_work_']
    vision=values['_vision_']
    job=values['_job_']
    flex=values['_flex_']
    neg = 0
    pos = 0
    print(manage)
    words = manage.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


       
    mpos=int(pos)*100/len(words)
    print('Positive: ' + str(mpos)+'%')
    print('Negative: ' + str(float(neg)*100/len(words))+'%')
    mneg=int(neg)*100/len(words)
    neg=0
    pos=0
    print(grow)
    words = grow.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


         
    print('Positive: ' + str(float(pos)*100/len(words))+'%')
    print('Negative: ' + str(float(neg)*100/len(words))+'%')
    gpos=int(pos)*100/len(words)
    gneg=int(neg)*100/len(words)
    neg=0
    pos=0
    print(work)
    words = work.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


         
    print('Positive: ' + str(float(pos)*100/len(words))+'%')
    print('Negative: ' + str(float(neg)*100/len(words))+'%')
    wpos=int(pos)*100/len(words)
    wneg=int(neg)*100/len(words)
    neg=0
    pos=0
    print(vision)
    words = vision.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


         
    print('Positpive: ' + str(float(pos)*100/len(words))+'%')
    print('Negatpive: ' + str(float(neg)*100/len(words))+'%')
    vpos=int(pos)*100/len(words)
    vneg=int(neg)*100/len(words)
    neg=0
    pos=0
    print(job)
    words = job.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


         
    print('Positive: ' + str(float(pos)*100/len(words))+'%')
    print('Negative: ' + str(float(neg)*100/len(words))+'%')
    jpos=int(pos)*100/len(words)
    jneg=int(neg)*100/len(words)

    neg=0
    pos=0
    print(flex)
    words = flex.split(' ')
    for word in words:
      classResult = classifier.classify( word_feats(word))
      if classResult == 'neg':
        neg = neg + 1
      if classResult == 'pos':
        pos = pos + 1


         
    fpos=int(pos)*100/len(words)
    print('Positive: ' + str(fpos)+'%')
    print('Negative: ' + str(float(neg)*100/len(words))+'%')
    fneg=int(neg)*100/len(words)
    #print(fpos)
    if com=='Company_1':
      p= [com, manage, grow, work, vision, job, flex, mpos, gpos, wpos, vpos, jpos, fpos, mneg, gneg, wneg, vneg, jneg, fneg]
      with open('com_1review.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(p)
      csvfile.close()

      df= pd.read_csv('com_1review.csv')
      #col=df.column('company')
      print(df)
     # print(col)
    if com=='Company_2':
      p= [com, manage, grow, work, vision, job, flex, mpos, gpos, wpos, vpos, jpos, fpos, mneg, gneg, wneg, vneg, jneg, fneg]
      with open('com_2review.csv','a') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(p)
      csvfile.close()

      df= pd.read_csv('com_2review.csv')
      print(df)
  


  #Barchart
  N = 6
  b=20
  a=b
  menMeans = (mpos, gpos, wpos, vpos, jpos, fpos)
  #menMeans = (fpos, 35, 30, 35, 27, 20)
  #womenMeans = (25, 32, 34, 20, 25,40)
  womenMeans = (mneg, gneg, wneg, vneg, jneg, fneg)
  menStd = (1, 1, 1, 1, 1,1)
  womenStd = (1, 1, 1, 1, 1, 1)
  ind = np.arange(N)    # the x locations for the groups
  width = 0.35       # the width of the bars: can also be len(x) sequence

  p1 = plt.bar(ind, menMeans, width, yerr=menStd)
  p2 = plt.bar(ind, womenMeans, width,
               bottom=menMeans, yerr=womenStd)

  plt.ylabel('Sentiment')
  plt.title('Sentimental Analysis')
  plt.xticks(ind, ('Management', 'Growth Opportunities', 'Work Culture', 'Value and Vision', 'Job Satisfaction','Flexibility'))

  plt.yticks(np.arange(0, 120, 20))
  plt.legend((p1[0], p2[0]), ('Positive', 'Negative'))

  plt.show()

  
  #posit = str(float(pos)*100/len(words))
  #negat= str(float(neg)*100/len(words))
  #your_float = 3.6
  #your_stringa = str(float(pos)*100/len(words))
  #your_stringb = str(float(neg)*100/len(words))

    #menMeans = (mpos, gpos, wpos, vpos, jpos, fpos)
  #womenMeans = (mneg, gneg, wneg, vneg, jneg, fneg)

