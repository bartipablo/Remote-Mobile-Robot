from paho.mqtt import client as mqtt
from conf import RASPBERRYPI5_IP


def initialize_mqtt_connection(message_callback):
    
    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"Connected to MQTT broker with result code {reason_code}")


    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = message_callback

    try:
        mqttc.connect(RASPBERRYPI5_IP, 1883, 60)
    except Exception as e:
        print(f"Cannot connect to MQTT broker.")
        print(f"Details: {e}")
        exit(1)
    
    return mqttc
