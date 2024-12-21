from view import MainView
from robot import Robot
from mqtt import initialize_mqtt_connection
from camera import Camera
import threading

robot = Robot()

def mqtt_on_connect_config(client, userdata, flags, reason_code, properties):
    client.subscribe("robot/battery/voltage", qos=0)

def mqtt_on_message_config(client, userdata, message):
    if message.topic == "robot/battery/voltage":
        payload = message.payload.decode('utf-8')
        robot.set_battery_voltage(float(payload))

mqttc = initialize_mqtt_connection(mqtt_on_message_config)

mqttc.on_connect = mqtt_on_connect_config

robot.set_mqtt_client(mqttc)

mqttc.loop_start()

camera = Camera(robot, mqttc)

camera_thread = threading.Thread(target=camera.receive_image_from_camera)
camera_thread.daemon = True
camera_thread.start()

app = MainView(robot, camera)
app.mainloop()
