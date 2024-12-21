from utils import get_wifi_signal_strength
from utils import get_ip_address

class Robot:
    def __init__(self):
        self.__battery_lvl = None
        self.__speed = 1
        self.__camera_turned_on = False

    def set_mqtt_client(self, mqttc):
        self.mqttc = mqttc

    def set_battery_voltage(self, battery_lvl):
        self.__battery_lvl = battery_lvl

    def get_battery_voltage(self):
        return self.__battery_lvl

    def speed_up(self):
        if self.get_speed() < 10:
            self.__speed += 1

    def speed_down(self):
        if self.get_speed() > 1:
            self.__speed -= 1

    def get_speed(self):
        return self.__speed

    def get_signal_strength(self):
        return get_wifi_signal_strength()
    
    def is_camera_turned_on(self):
        return self.__camera_turned_on
    
    def switch_camera(self):
        self.__camera_turned_on = not self.__camera_turned_on

        if self.mqttc:
            if self.__camera_turned_on:
                self.mqttc.publish("robot/camera/connect", get_ip_address(), qos=1)
            else:
                self.mqttc.publish("robot/camera/disconnect", get_ip_address(), qos=1)

        return self.__camera_turned_on

    def enable_buzzer(self):
        self.mqttc.publish("robot/control/buzzer", "on", qos=0)
        