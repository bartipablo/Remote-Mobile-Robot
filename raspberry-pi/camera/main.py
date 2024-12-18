import socket
import time
import cv2
from picamera2 import Picamera2
import pickle
from paho.mqtt import client as mqtt

from config import (
    CLIENT_SOCKET_PORT,
    MQTT_PORT,
    MQTT_IPv4,
)
from utils import is_valid_ipv4_address

clients_ip = set()


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to MQTT broker with result code {reason_code}")
    client.subscribe("robot/camera/connect", qos=1)
    client.subscribe("robot/camera/disconnect", qos=1)


def on_message(client, userdata, msg):
    global clients_ip

    if msg.topic == "robot/camera/connect":
        payload = msg.payload.decode('utf-8')

        print("Connect to camera request received.")
        print(f"Delivered IP: {payload}")

        if not is_valid_ipv4_address(payload):
            print("Rejected. Invalid IP address.")
            return

        clients_ip.add(payload)
        print("Connected to camera.")

    elif msg.topic == "robot/camera/disconnect":
        payload = msg.payload.decode('utf-8')
        print("Disconnect from camera request received.")
        print(f"Delivered IP: {payload}")

        clients_ip.discard(payload)


def configure_mqtt(mqttc):
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect(MQTT_IPv4, MQTT_PORT, 60)
    mqttc.loop_start()


def configure_camera(camera):
    camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
    camera.start()


if __name__ == "__main__":
    print("Starting raspberryPi robot camera...")

    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    configure_mqtt(mqttc)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    picam2 = Picamera2()
    configure_camera(picam2)

    try:
        while True:
            if  len(clients_ip) == 0:
                time.sleep(0.5)
                continue

            img = picam2.capture_array()
            img = cv2.rotate(img, cv2.ROTATE_180)

            ret, buffer = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 30])

            x_as_bytes = pickle.dumps(buffer)
            for ipv4 in clients_ip.copy():
                sock.sendto(x_as_bytes, (ipv4, CLIENT_SOCKET_PORT))

    except KeyboardInterrupt:
        print("Program terminated by user.")
    except Exception as e:
        print("Unexpected error occurred.")
        print(f"Details: {e}")
    finally:
        sock.close()
        picam2.stop()
