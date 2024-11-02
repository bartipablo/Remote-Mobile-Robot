from view import MainView
from robot import Robot
from mqtt import initialize_mqtt_connection
from camera import Camera
import threading

robot = Robot()

mqttc = initialize_mqtt_connection(lambda message: print(f"Wiadomość: {message}"))

mqtt_thread = threading.Thread(target=mqttc.loop_forever)
mqtt_thread.daemon = True
mqtt_thread.start()

camera = Camera(robot, mqttc)

camera_thread = threading.Thread(target=camera.receive_image_from_camera)
camera_thread.daemon = True
camera_thread.start()

app = MainView(robot, camera)
app.mainloop()
