import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
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
  
layout = [[sg.Text('Welcome to EMPLOYEE EVALUATION', size=(29, 1), font=("Helvetica", 25))],
    [sg.Text('Here you can add employee details and review')],
    [sg.Text('Name of Employee:'),sg.InputText(key='_name_')],
    [sg.Text('Departments:'),sg.Listbox(('Eots','Telemetry','Radar and meteorology','CAN','CDP','Control and Timing','Flight Safety','Mission Coordination','Power System'), size=(20, 3),key='_depart_')],
    [sg.Text('Designation:'),sg.InputCombo(('Sci-A','Sci-B','Sci-C','Sci-D','Sci-E','Sci-F','Sci-G','Fellowship','Apprentice'), size=(20, 3),key='_desig_')],
    [sg.Text('Reviews:'),sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(20, 3),key='_INPUT_')],
    [sg.Text('Projects Undertaken')],
    [sg.Text('Jan-March:'),sg.InputText(key='_pjm_'),sg.Text('April-June:'),sg.InputText(key='_paj_')],
    [sg.Text('July-Sept:'),sg.InputText(key='_pjs_'),sg.Text('Oct-Dec:'),sg.InputText(key='_pod_')],
    [sg.Submit('upload',key='_OK BUTTON_'), sg.Cancel()],
    [sg.Text('_'  * 80)],
    [sg.Output(size=(80, 10))]]  
  



positive_vocab = [ 'awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great','top','pure','motivated','talented', 'hate','avoid',':)' ]
negative_vocab = [ 'bad', 'terrible','useless', 'hate','avoid','hatred','idiot','worse',':(' ]
neutral_vocab = [ 'movie','the','sound','was','is','actors','did','know','words','not' ]

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab] 
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]   
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]
train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set) 

# Predict
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
  		pjm=values['_pjm_']
  		paj=values['_paj_']
  		pjs=values['_pjs_']
  		pod=values['_pod_']
  		sentence=values['_INPUT_']
  		sentence=sentence.lower()
  		print('Employee Name:'+str(name)+'.')
  		print('Department:'+str(depart)+'.')
  		print('Designation:'+str(desig)+'.')
  		print(pjm)
  		words = sentence.split(' ')
  		for word in words:
		    classResult = classifier.classify( word_feats(word))
		    if classResult == 'neg':
			        neg = neg + 1
		    if classResult == 'pos':
			        pos = pos + 1


       
  print('Positive: ' + str(float(pos)*100/len(words))+'%')
  print('Negative: ' + str(float(neg)*100/len(words))+'%')
  posit = str(float(pos)*100/len(words))
  negat= str(float(neg)*100/len(words))
  your_float = 3.6
  your_stringa = str(float(pos)*100/len(words))
  your_stringb = str(float(neg)*100/len(words))

  # Data to plot
  p = float(your_stringa) * your_float
  n = float(your_stringb) * your_float
  labels = 'Positive', 'Negative'
  sizes = [p,n]
  colors = ['yellowgreen', 'lightskyblue']
  explode = (0.1, 0)  # explode 1st slice


  # Plot
  plt.subplot(221)
  plt.pie(sizes, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=140)
  plt.axis('equal')
  
  #bar plot

  Pjm=int(pjm)
  Paj=int(paj)
  Pjs=int(pjs)
  Pod=int(pod)
  objects = ('Jan-March', 'April-June', 'July-Sept', 'Oct-Dec')
  y_pos = np.arange(len(objects))
  performance = [Pjm,Paj,Pjs,Pod]
  plt.subplot(222)
  plt.bar(y_pos, performance, align='center', alpha=0.5)
  plt.xticks(y_pos, objects)
  plt.ylabel('Usage')
  plt.title('Projects Undertaken')

  plt.show()		
 