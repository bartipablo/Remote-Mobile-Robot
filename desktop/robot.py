from wifi import get_wifi_signal_strength


class Robot:
    def __init__(self):
        self.__battery_lvl = 19
        self.__speed = 1
        self.__camera_turned_on = False

    def set_battery_lvl(self, battery_lvl):
        if battery_lvl < 0:
            self.__battery_lvl = 0
            return

        if battery_lvl > 100:
            self.__battery_lvl = 100
            return

        self.__battery_lvl = battery_lvl

    def get_battery_lvl(self):
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

