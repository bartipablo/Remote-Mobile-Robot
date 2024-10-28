class Controller:
    def __init__(self, view, robot):
        self.view = view
        self.robot = robot

    def pressed_keys_handler(self, pressed_keys):
        if 'H' in pressed_keys:
            print("PRESSED H")
        if 'L' in pressed_keys:
            print("PRESSED L")

        if 'Up' in pressed_keys:
            self.robot.speed_up()
            self.view.update_speed_label(self.robot.get_speed())

        elif 'Down' in pressed_keys:
            self.robot.speed_down()
            self.view.update_speed_label(self.robot.get_speed())

        if 'W' in pressed_keys and 'A' in pressed_keys:
            print("PRESSED W and A")

        elif 'W' in pressed_keys and 'D' in pressed_keys:
            print("PRESSED W and D")

        elif 'S' in pressed_keys and 'A' in pressed_keys:
            print("PRESSED S and A")

        elif 'S' in pressed_keys and 'D' in pressed_keys:
            print("PRESSED S and D")

        elif 'W' in pressed_keys and 'S' in pressed_keys:
            print("PRESSED W and S")

        elif 'W' in pressed_keys:
            print("PRESSED W")

        elif 'A' in pressed_keys:
            print("PRESSED A")

        elif 'S' in pressed_keys:
            print("PRESSED S")

        elif 'D' in pressed_keys:
            print("PRESSED D")

        elif 'Left' in pressed_keys and 'Right' in pressed_keys:
            print("PRESSED LEFT and RIGHT")

        elif 'Left' in pressed_keys:
            print("PRESSED LEFT")

        elif 'Right' in pressed_keys:
            print("PRESSED RIGHT")

