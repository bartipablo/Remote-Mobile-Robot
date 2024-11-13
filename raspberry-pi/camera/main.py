import socket
import time
import cv2
from picamera2 import Picamera2
import pickle
from paho.mqtt import client as mqtt

PORT = 5054
client_IP_address = None


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to MQTT broker with result code {reason_code}")
    client.subscribe("robot/camera", qos=1)


def on_message(client, userdata, msg):
    global client_IP_address
    if msg.topic == "robot/camera":
        payload = msg.payload.decode('utf-8')
        
        parts = payload.split('/', 1)
        if len(parts) != 2:
            return

        action, ip_address = parts

        if action == "disconnect":
            print(f"Camera is turned off for ip address: {ip_address}")
            if client_IP_address == ip_address:
                client_IP_address = None
        elif action == "connect":
            print(f"Camera is turned on. Client IP address: {ip_address}")
            client_IP_address = ip_address
        else:
            print(f"Unknown action: {action}")


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("192.168.10.1", 1883, 60)
mqttc.loop_start()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

try:
    while True:        
        if client_IP_address is None:
            time.sleep(0.5)
            continue

        try:
            img = picam2.capture_array()
            ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])

            x_as_bytes = pickle.dumps(buffer)
            sock.sendto(x_as_bytes, (client_IP_address, PORT))
        except TypeError:
            client_IP_address = None

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    sock.close()
    picam2.stop()
