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
    next(reader) # skip header
    posi = [r for r in reader]
#print(posi) '''
import PySimpleGUI as sg  

sg.ChangeLookAndFeel('Dark')
layout = [[sg.Text(' EMPLOYEE EVALUATION', size=(29, 1), font=("Helvetica", 25))],
    [sg.Text('EMPLOYEES BASIC DATA')],
    [sg.Text('Name of Employee:'),sg.InputText(key='_name_')],
    [sg.Text('Departments:'),sg.OptionMenu(('HR','Management','Sales','Executive','Technical','Research & development'), size=(20, 3),key='_depart_'),sg.Text('Designation:'),sg.OptionMenu(('Software Engineer','Program analyst','system analyst','project head','program manager','Trainee engineer'), size=(20, 3),key='_desig_')],
    [sg.Text('Professional PARAMETER RATINGS', size=(29, 1), font=("Helvetica", 25))], 
    [sg.Text('Quality of work'),sg.InputCombo(('good','satisfactory','good bad','terrible','poor'), size=(20, 3),key='_work_'),sg.Text('Productivity'),sg.InputCombo(('good','satisfactory','good bad','terrible','poor'), size=(20, 3),key='_pro_')],
    [sg.Text('Punctuality    '),sg.InputCombo(('good','satisfactory','good bad','terrible','poor'), size=(20, 3),key='_punct_'),sg.Text('Performance'),sg.InputCombo(('good','satisfactory','good bad','terrible','poor'), size=(20, 3),key='_per_')],
    [sg.Text('Professional ethics'),sg.InputCombo(('good','satisfactory','good bad','terrible','poor'), size=(20, 3),key='_ethics_')],
    [sg.Text('Reviews:'),sg.Multiline(default_text='Enter your review', size=(20, 3),key='_INPUT_')],
    [sg.Submit('upload',key='_OK BUTTON_'), sg.Cancel()],
    [sg.Text('_'  * 80)],
    #[sg.T('0%',key='output'), sg.ProgressBar(100, orientation='h', size=(40,40), bar_color=('red', 'yellow green'), relief=sg.RELIEF_RAISED  ,key='progress')],
    [sg.Output(size=(80, 10))]]  


positive_vocab = ['satisfactory', 'awesome', 'outstanding', 'okay', 'fantastic','good', 'nice', 'great','top','motivated','talented', 'hate','avoid','perfect','high' ]
negative_vocab = [ 'terrible','bad', 'terrible','okay', 'hate','avoid','hatred','idiot','worse','late','poor','unproductive','lazy','very poor','under rated' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not','average',]

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab] 
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]   
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set) 



neg = 0
pos = 0



window = sg.Window('Get filename example').Layout(layout)  
  
# The Event Loop  
while True:  
  event, values = window.Read()  
  if event is None:  
        break  
  if event == '_OK BUTTON_':
  		name=values['_name_']
  		depart=values['_depart_']
  		desig=values['_desig_']
  		work=values['_work_']
  		pro=values['_pro_']
  		punct=values['_punct_']
  		per=values['_per_']
  		ethics=values['_ethics_'] 
  		sentence=values['_INPUT_']
  		sentence=sentence.lower()
  		print('Employee Name:'+str(name)+'.')
  		print('Department:'+str(depart)+'.')
  		print('Designation:'+str(desig)+'.')
  		print('Quality of work:'+str(work)+'.')
  		print('Productivity:'+str(pro)+'.')
  		print('Punctuality:'+str(punct)+'.')
  		print('Performance:'+str(per)+'.')
  		print('Professional ethics:'+str(ethics)+'.')
  		words = sentence.split(' ')
  		for word in words:
		    classResult = classifier.classify( word_feats(word))
		    if classResult == 'neg':
			        neg = neg + 1
		    if classResult == 'pos':
			        pos = pos + 1
	    

  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  preview=float(pos)*100/len(words)
  nreview=float(neg)*100/len(words)
  pos=0
  neg=0
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
  wp=float(pos)*100/len(words)
  wn=float(neg)*100/len(words)
  pos=0
  neg=0
  print(pro)
  words = pro.split(' ')
  for word in words:
  	classResult = classifier.classify( word_feats(word))
  	if classResult == 'neg':
  		neg = neg + 1
  	if classResult == 'pos':
  		pos = pos + 1
  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  prop=float(pos)*100/len(words)
  pron=float(neg)*100/len(words)

  pos=0
  neg=0
  print(punct)
  words = punct.split(' ')
  for word in words:
  	classResult = classifier.classify( word_feats(word))
  	if classResult == 'neg':
  		neg = neg + 1
  	if classResult == 'pos':
  		pos = pos + 1
  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  punctp=float(pos)*100/len(words)
  punctn=float(neg)*100/len(words)
  pos=0
  neg=0
  print(per)
  words = per.split(' ')
  for word in words:
  	classResult = classifier.classify( word_feats(word))
  	if classResult == 'neg':
  		neg = neg + 1
  	if classResult == 'pos':
  		pos = pos + 1
  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  perp=float(pos)*100/len(words)
  pern=float(neg)*100/len(words)
  pos=0
  neg=0
  print(ethics)
  words = ethics.split(' ')
  for word in words:
  	classResult = classifier.classify( word_feats(word))
  	if classResult == 'neg':
  		neg = neg + 1
  	if classResult == 'pos':
  		pos = pos + 1
  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  ethicsp=float(pos)*100/len(words)
  ethicsn=float(neg)*100/len(words)
  result=((wp+prop+perp+punctp+ethicsp-wn-pron-pern-punctn-ethicsn)/5)

  presult=((wp+prop+perp+punctp+ethicsp)/5)
  pp=int((presult+preview)*1.8)
  nresult=((wn+pron+pern+punctn+ethicsn)/5)
  np=int((nresult+nreview)*1.8)
  print(presult,nresult)
  a=sentence
  p= [name,depart,desig,wp,prop,punctp,perp,ethicsp,wn,pron,punctn,pern,ethicsn,presult,nresult,a,nreview,preview]
  with open('positive.csv','a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(p)
  csvfile.close()

  df= pd.read_csv('positive.csv')
  print(df)
  # Data to plot
  labels = 'Positive', 'Negative'
  sizes = [pp, np]
  colors = ['gold', 'yellowgreen']
  explode = (0.1, 0)  # explode 1st slice

  # Plot
  plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)

  plt.axis('equal')
  plt.show()

window.Close()



    