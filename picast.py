'''
author: zabiralnazi@yahoo.com
'''
# picast
from vidgear.gears import PiGear
import cv2
import socket
from vidgear.gears import NetGear
import json

# class piclient

class piclient:

    def __init__(self, ip = '192.168.10.50', port_1 = 10000, port_2 = 5454, time_delay = 1, frame_rate = 25, img_resolution = (320, 240)):


        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.server_address = (ip, port_1)

        self.options = {"hflip": True, "exposure_mode": "auto", "iso": 800, "exposure_compensation": 15,
            "awb_mode": "horizon", "sensor_mode": 0}  

        self.stream = PiGear(resolution=img_resolution, framerate=frame_rate, time_delay=time_delay,  logging=True,
                        **self.options).start() 


        self.server = NetGear(address = ip,
                        port = port_2, protocol = 'tcp',
                        pattern = 0, receive_mode = False,
                        logging = True, flag = 0, copy = False, track = False) 

    def send_data(self, image_capture = True, json_data = {"data": None}):
        if image_capture:
            try:
                frame = self.stream.read()
                self.server.send(frame)
            except:
                print('frame sending failed!')
        
        try:
            send_data = json.dumps(json_data)
            s_text = str(send_data)

            message = bytes(s_text, encoding = 'utf-8')

            self.sock.sendto(message, self.server_address)

        except:
            print('data sending failed!')
            #pass

    def close(self):
        self.stream.stop()
        self.server.close()
        print('connection closed!')


class server:

    def __init__(self, ip = '192.168.10.50', port_1 = 10000, port_2 = 5454):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.server_address = (ip, port_1)
        self.sock.bind(self.server_address)
        self.client = NetGear(address = ip, port = port_2, protocol = 'tcp',  pattern = 0, receive_mode = True, logging = True, flag = 0, copy  =False, track = False)

    def receive_data(self, image_capture = True):
        if image_capture:
            frame = self.client.recv()
        data, address = self.sock.recvfrom(100) # blocking IO
        data = json.loads(data)

        return frame, data, address





