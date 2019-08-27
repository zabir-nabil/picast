from picast import server
import cv2

my_server = server(ip = '192.168.10.50', port_1 = 10000, port_2 = 5454)

while True:
	a, b, c = my_server.receive_data()
	# data
	print(b)
	# address
	print(c)

	cv2.imshow("Picast Demo", a) # image

	key = cv2.waitKey(1) & 0xFF
	# check for 'q' key-press
	if key == ord("q"):
		#if 'q' key-pressed break out
		break

cv2.destroyAllWindows()