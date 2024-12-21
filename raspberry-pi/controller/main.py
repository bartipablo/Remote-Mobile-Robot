import serial
from paho.mqtt import client as mqtt
from config import MQTT_IPv4, MQTT_PORT
from robot import Robot


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected to MQTT broker with result code {reason_code}")
    client.subscribe("robot/control/buzzer", qos=0)


def on_message(client, userdata, msg):
    robot = userdata

    try:
        if msg.topic == "robot/control/buzzer":
            robot.enable_buzzer()

        elif msg.topic == "robot/move/forward":
            robot.move_forward(int(msg.payload))

        elif msg.topic == "robot/move/backward":
            robot.move_backward(int(msg.payload))

        elif msg.topic == "robot/move/left":
            robot.move_left(int(msg.payload))

        elif msg.topic == "robot/move/right":
            robot.move_right(int(msg.payload))

        elif msg.topic == "robot/move/forward-left":
            robot.move_forward_left(int(msg.payload))

        elif msg.topic == "robot/move/forward-right":
            robot.move_forward_right(int(msg.payload))

        elif msg.topic == "robot/move/backward-left":
            robot.move_backward_left(int(msg.payload))
        
        elif msg.topic == "robot/move/backward-right":
            robot.move_backward_right(int(msg.payload))

        elif msg.topic == "robot/move/rotate-left":
            robot.rotate_left(int(msg.payload))

        elif msg.topic == "robot/move/rotate-right":
            robot.rotate_right(int(msg.payload))
    except Exception as e:
        print(f"Error during reading message from client.")
        print("f Details: {e}")


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
    mqttc.loop_forever()
