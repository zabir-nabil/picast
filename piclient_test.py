from picast import piclient
import random

my_client = piclient(ip = '192.168.10.50', port_1 = 10000, port_2 = 5454, time_delay = 1, frame_rate = 25, img_resolution = (320, 240))

print('piclient initiated')
sensor_val = 1
while True:
    my_client.send_data(json_data = {'sensor_val': sensor_val})
    sensor_val = (random.randint(0,500))
    

