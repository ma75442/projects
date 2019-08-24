import  PySimpleGUI as sg
import micInput as mi
import time
import single_pred as sd
import addNewData as ad


#GUI

layout = [[sg.Text('EOTS', font='Helvetica 15')],
          [sg.ReadButton('Speak')],
          [sg.Button('abort', button_color=('black','firebrick3'), key='abort'),
           sg.Button('activate', button_color=('black','firebrick3'), key='activate'),
           sg.Button('launch', button_color=('black','firebrick3'), key='launch'),
           sg.Button('switch', button_color=('black','firebrick3'), key='switch'),
           sg.Button('zoom', button_color=('black','firebrick3'), key='zoom'),
           sg.Button('track', button_color=('black','firebrick3'), key='track'),
           sg.Button('egde', button_color=('black','firebrick3'), key='egde'),
           sg.Button('centroid', button_color=('black','firebrick3'), key='centroid')],
          [sg.Output(size=(80, 10))],
          [sg.Exit()]]

window = sg.Window('Speech Recognition').Layout(layout)

i=[0,0,0,0,0,0,0,0]

def but_recog(v):
  if v=='abort':
      colour_change('abort',i[0])
      i[0]+=1
  elif v=='activate':
    colour_change('activate',i[1])
    i[1]+=1
  elif v=='centroid':
    colour_change('centroid',i[2])
    i[2]+=1
  elif v=='edge':
    colour_change('edge',i[3])
    i[3]+=1
  elif v=='launch':
    colour_change('launch',i[4])
    i[4]+=1
  elif v=='switch':
    colour_change('switch',i[5])
    i[5]+=1
  elif v=='track':
    colour_change('track',i[6])
    i[6]+=1
  elif v=='zoom':
    colour_change('zoom',i[7])
    i[7]+=1

def colour_change(command,x):
  if x%2==0:
    window.FindElement(command).Update(button_color=('gray34','black'))
  else:
    window.FindElement(command).Update(button_color=('black','firebrick3'))



while True:
  event,values = window.Read()
  if event is None or event == 'Exit':
      break
  elif event == 'Speak':
    print('Recording...')
    mi.mic()
    window.Refresh()
    print('Done...')
    v = sd.sip()
    but_recog(v)

    window.Refresh()
    
    choice = sg.PopupGetText('Choose the actual command: 1-abort  2-activate  3-centroid  4-edge  5-launch  6-switch  7-track  8-zoom',
      default_text='',size=(30,30),background_color=None,button_color=(None,None),no_titlebar=True,keep_on_top=False,location=(500,500))
    
    ad.aNd(choice)
    window.Refresh()
  
  elif event=='abort':
      colour_change('abort',i[0])
      i[0]+=1
  elif event=='activate':
    colour_change('activate',i[1])
    i[1]+=1
  elif event=='centroid':
    colour_change('centroid',i[2])
    i[2]+=1
  elif event=='edge':
    colour_change('edge',i[3])
    i[3]+=1
  elif event=='launch':
    colour_change('launch',i[4])
    i[4]+=1
  elif event=='switch':
    colour_change('switch',i[5])
    i[5]+=1
  elif event=='track':
    colour_change('track',i[6])
    i[6]+=1
  elif event=='zoom':
    colour_change('zoom',i[7])
    i[7]+=1

      
window.Close()