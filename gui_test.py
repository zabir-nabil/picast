import PySimpleGUI as sg
import cv2
from PIL import Image
import io
from sys import exit as exit

from picast import server
my_server = server(ip = '192.168.10.50', port_1 = 10000, port_2 = 5454)


layout = [[sg.Text('Raspberry PI Sensor Value:'), sg.Text('', size=(15,1), key='_OUTPUT_')],
          #[sg.Input(key='_IN_')],
          [sg.Image(filename='', key='image')],
          [sg.Button('Exit')]]

window = sg.Window('Picast Demo', layout)

cnt = 0
while True:  # Event Loop
    event, values = window.Read(timeout=0)
    a, b, c = my_server.receive_data()
    # print(event, values)
    window.Element('_OUTPUT_').Update(str(b))
    cnt += 1
    if event is None or event == 'Exit':
        break

    gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

    # let img be the PIL image
    img = Image.fromarray(gray)  # create PIL image from frame
    bio = io.BytesIO()  # a binary memory resident stream
    img.save(bio, format= 'PNG')  # save image as png to it
    imgbytes = bio.getvalue()  # this can be used by OpenCV hopefully
    window.FindElement('image').Update(data=imgbytes)

window.Close()