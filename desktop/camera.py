import socket
import pickle
import cv2
from conf import SOCKET_PORT


class Camera:
    def __init__(self, robot, mqttc):
        self.robot = robot
        self.mqttc = mqttc
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def receive_image_from_camera(self):        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.bind(('', SOCKET_PORT))

        while True:            
            data, addr = sock.recvfrom(1000000)

            if not self.robot.is_camera_turned_on():
                continue

            img_data = pickle.loads(data)

            img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            
            if self.callback:
                self.callback(img)
