import serial
from paho.mqtt import client as mqtt
from config import MQTT_IPv4, MQTT_PORT
from robot import Robot


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to MQTT broker with result code {reason_code}")
    client.subscribe("robot/control/buzzer", qos=0)


def on_message(client, userdata, msg):
    robot = userdata

    if msg.topic == "robot/control/buzzer":
        robot.enable_buzzer()


if __name__ == "__main__":
    print("Starting raspberryPi robot controller...")
    
    # Configure serial communication
    ser = serial.Serial("/dev/ttyS0", 500000)

    robot = Robot(ser)

    # Configure MQTT client
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect(MQTT_IPv4, MQTT_PORT, 60)
    mqttc.user_data_set(robot)
    mqttc.loop_start()
