import serial
from paho.mqtt import client as mqtt
from config import MQTT_IPv4, MQTT_PORT


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print("Starting raspberryPi battery measure...")

    try:
        ser = serial.Serial("/dev/ttyS0", 500000, timeout=1)

        mqttc = mqtt.Client()
        mqttc.connect(MQTT_IPv4, MQTT_PORT, 60)

        while True:
            try:
                voltage = ser.readline().decode("utf-8").strip()
                if voltage and is_number(voltage):
                    mqttc.publish("robot/battery/voltage", voltage, qos=0)
            except Exception as e:
                print(f"Error reading serial data: {e}")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user (Ctrl+C). Exiting...")

    finally:
        try:
            ser.close()
        except:
            pass
        try:
            mqttc.disconnect()
        except:
            pass
        print("Resources closed. Program terminated.")
