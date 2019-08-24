import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import PySimpleGUI as sg  
c1p=0
c1n=0
c2p=0
c2n=0
sg.ChangeLookAndFeel('Dark')
layout = [[sg.Text(' Company Evaluation', size=(29, 1), font=("Helvetica", 25))],
    [sg.ReadButton('Company_1',key='_OK_'), sg.ReadButton('Company_2',key='_button_'), sg.ReadButton('Compare',key='_bon_')],
    [sg.Text('_'  * 80)],
    #[sg.T('0%',key='output'), sg.ProgressBar(100, orientation='h', size=(40,40), bar_color=('red', 'yellow green'), relief=sg.RELIEF_RAISED  ,key='progress')],
    [sg.Output(size=(80, 10))]]
window = sg.Window('Get filename example').Layout(layout)  
  
# The Event Loop  
while True:  
  event, values = window.Read()  
  if event is None:  
        break  
  if event == '_OK_':
    print('Done')
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
    presultt=(mpost+gpost+wpost+vpost+jpost+fpost)*0.6  #3.6/6
    c1p=presultt
    print(c1p)
    nresultt=(mnegt+gnegt+wnegt+vnegt+jnegt+fnegt)*0.6
    c1n=nresultt
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
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Overall rating')
    plt.show()
  if event == '_button_':
    print('Done')
    df= pd.read_csv('com_2review.csv')
    print(df)
    l=len(df)
    col=df.mpos
    print(l)
      #positive response
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
    c2p=presultt
    nresultt=(mnegt+gnegt+wnegt+vnegt+jnegt+fnegt)*0.6
    c2n=nresultt
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
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Overall rating')
    plt.show()
  if event == '_bon_':
    plt.subplot(1,2,1)
    labels = 'company1', 'Company2'
    sizes = [c1p, c2p]
    colors = ['cyan', 'red']
    explode = (0.1, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Overall company rating(positive)')
    plt.subplot(1,2,2)
    labels = 'company1', 'Company2'
    sizes = [c1n, c2n]
    colors = ['grey', 'blue']
    explode = (0.1, 0)  # explode 1st slice
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Overall company rating(negative)')
    plt.show()

window.Close()