class Robot:
    def __init__(self):
        self.battery_lvl = None
        self.speed = 1

    def set_battery_lvl(self, battery_lvl):
        if battery_lvl < 0:
            self.battery_lvl = 0
            return

        if battery_lvl > 100:
            self.battery_lvl = 100
            return

        self.battery_lvl = battery_lvl

    def get_battery_lvl(self):
        return self.battery_lvl

    def set_speed(self, speed):
        if speed < 1:
            self.speed = 1
            return

        if speed > 10:
            self.speed = 10
            return

        self.speed = speed

    def get_speed(self):
        return self.speed