import pywhatkit
import PySimpleGUI as sg
import random

layout = [[sg.Text("Select The Text file: ", size=(30,1))],
          [sg.Input(key='-INPUT1-'),sg.FileBrowse(file_types=(("TXT Files", "*.txt"), ("ALL Files", "*.*")))],
          [sg.Text("Save Output to: ", size=(30,1))],
          [sg.Input(key='-INPUT2-'),sg.FileSaveAs("Save to",key='img_save',file_types=(('JPG', '.jpg'),('PNG', '.png')))],
          [sg.Button("Convert",size=(15,2)),sg.Button("Exit",size=(10,2))]]

window = sg.Window("Text to Handwriting   (!!! Email: vaumtol@gmail.com !!!)",layout,size=(800,250))
while True:
    event, values = window.Read()
    if event == 'Convert':
        filename1 = values['-INPUT1-']
        filename2= values['-INPUT2-']
        if filename1 =='':
            sg.popup("Select Text file")
            continue
        elif filename2 == '':
            sg.popup("Select Output Location")
            continue
        else:
            try:
               f = open(filename1, "r")
               j = f.read()
               pywhatkit.text_to_handwriting(j, save_to= filename2, rgb=(0, 0, 138))
               sg.popup("Done",text_color='Yellow')
            except:
               sg.popup("Unexpected Error",text_color='red')

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
window.close()
