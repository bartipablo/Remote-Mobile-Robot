import tkinter as tk
from wifi import get_wifi_signal_strength
import controller as ctrl


class MainView(tk.Tk):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        self.key_labels = {}
        self.signal_bar_labels = {}
        self.battery_bar_labels = {}
        self.speed_label = None

        self.pressed_keys = set()

        self.title("Remote robot control")
        self.geometry("1200x600")
        self.configure(bg="#343036")

        self.draw_manual()
        self.draw_state()

        self.bind("<KeyPress>", self.__on_key_press)
        self.bind("<KeyRelease>", self.__on_key_release)

    def draw_manual(self):
        manual_frame = tk.Frame(self, width=250, height=600, bg="#343036")
        manual_frame.pack(side="left", fill="both")
        self.__draw_control_manual(manual_frame)
        self.__draw_rotation_manual(manual_frame)
        self.__draw_speed_manual(manual_frame)
        self.__draw_play_sound_manual(manual_frame)
        self.__draw_switch_light_manual(manual_frame)

    def __draw_control_manual(self, frame):
        description_label = tk.Label(frame, text="Robot movement", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        description_label.pack(pady=10, padx=10)

        control_frame = tk.Frame(frame, bg="#343036")
        control_frame.pack(pady=0)

        move_forward_label = make_button_label("W", control_frame)
        move_forward_label.grid(row=0, column=1, padx=5, pady=5)
        self.key_labels["W"] = move_forward_label

        move_left_label = make_button_label("A", control_frame)
        move_left_label.grid(row=1, column=0, padx=5, pady=5)
        self.key_labels["A"] = move_left_label

        move_backward_label = make_button_label("S", control_frame)
        move_backward_label.grid(row=1, column=1, padx=5, pady=5)
        self.key_labels["S"] = move_backward_label

        move_right_label = make_button_label("D", control_frame)
        move_right_label.grid(row=1, column=2, padx=5, pady=5)
        self.key_labels["D"] = move_right_label

    def __draw_rotation_manual(self, frame):
        description_label = tk.Label(frame, text="Robot rotation", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        description_label.pack(pady=10, padx=10)

        rotation_frame = tk.Frame(frame, bg="#343036")
        rotation_frame.pack(pady=0)

        rotate_left_label = make_button_label("←", rotation_frame)
        rotate_left_label.grid(row=0, column=0, padx=5, pady=5)
        self.key_labels["Left"] = rotate_left_label

        rotate_right_label = make_button_label("→", rotation_frame)
        rotate_right_label.grid(row=0, column=1, padx=5, pady=5)
        self.key_labels["Right"] = rotate_right_label

    def __draw_speed_manual(self, frame):
        description_label = tk.Label(frame, text="Robot speed", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        description_label.pack(pady=10, padx=10)

        speed_frame = tk.Frame(frame, bg="#343036")
        speed_frame.pack(pady=0)

        increase_speed_label = make_button_label("↑", speed_frame)
        increase_speed_label.grid(row=0, column=0, padx=5, pady=5)
        self.key_labels["Up"] = increase_speed_label

        decrease_speed_label = make_button_label("↓", speed_frame)
        decrease_speed_label.grid(row=0, column=1, padx=5, pady=5)
        self.key_labels["Down"] = decrease_speed_label

    def __draw_play_sound_manual(self, frame):
        description_label = tk.Label(frame, text="Play sound", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        description_label.pack(pady=10, padx=10)

        sound_frame = tk.Frame(frame, bg="#343036")
        sound_frame.pack(pady=0)

        play_sound_label = make_button_label("H", sound_frame)
        play_sound_label.grid(row=0, column=0, padx=5, pady=5)
        self.key_labels["H"] = play_sound_label

    def __draw_switch_light_manual(self, frame):
        description_label = tk.Label(frame, text="Switch light", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        description_label.pack(pady=10, padx=10)

        light_frame = tk.Frame(frame, bg="#343036")
        light_frame.pack(pady=0)

        switch_light_label = make_button_label("L", light_frame)
        switch_light_label.grid(row=0, column=0, padx=5, pady=5)
        self.key_labels["L"] = switch_light_label

    def __update_key_label(self, label, pressed):
        if pressed:
            label.config(bg="#777777")
            label.config(fg="#000000")
        else:
            label.config(bg="#555555")
            label.config(fg="white")

    def draw_state(self):
        state_frame = tk.Frame(self, width=250, height=600, bg="#343036")
        state_frame.pack(side="right", fill="both")

        self.__draw_signal_strength(state_frame)
        self.__draw_battery_level(state_frame)
        self.__draw_speed(state_frame)

    def __draw_signal_strength(self, frame):
        def make_signal_bar_label(parent, height):
            return tk.Label(
                parent, bg="#555555",
                width=1, height=height, relief="raised", borderwidth=1
            )

        signal_strength_label = tk.Label(frame, text="Signal strength:", font=("Arial", 14, "bold"), fg="white",
                                         bg="#343036")
        signal_strength_label.pack(pady=10, padx=10)

        signal_strength_frame = tk.Frame(frame, bg="#343036")
        signal_strength_frame.pack(pady=0)

        for i in range(1, 6):
            self.signal_bar_labels[i] = make_signal_bar_label(signal_strength_frame, i)
            self.signal_bar_labels[i].grid(row=0, column=i, padx=2, pady=5, sticky='s')

    def __draw_battery_level(self, frame):
        def make_battery_bar_label(parent):
            return tk.Label(
                parent, bg="#555555",
                width=1, height=2, relief="raised", borderwidth=1
            )

        battery_level_label = tk.Label(frame, text="Battery level:", font=("Arial", 14, "bold"), fg="white",
                                         bg="#343036")
        battery_level_label.pack(pady=10, padx=10)

        battery_level_frame = tk.Frame(frame, bg="#343036")
        battery_level_frame.pack(pady=0)

        for i in range(1, 6):
            self.battery_bar_labels[i] = make_battery_bar_label(battery_level_frame)
            self.battery_bar_labels[i].grid(row=0, column=i, padx=0, pady=5)

        addition_battery_label = tk.Label(
            battery_level_frame, bg="white",
            width=1, height=1, relief="raised", borderwidth=1
        )
        addition_battery_label.grid(row=0, column=6, padx=1, pady=5)

    def __draw_speed(self, frame):
        speed_label = tk.Label(frame, text="Speed:", font=("Arial", 14, "bold"), fg="white", bg="#343036")
        speed_label.pack(pady=10, padx=10)

        speed_frame = tk.Frame(frame, bg="#343036")
        speed_frame.pack(pady=0)

        self.speed_label = tk.Label(speed_frame, text="1", font=("Arial", 20, "bold"), fg="white", bg="#343036")
        self.speed_label.grid(row=0, column=0, padx=5, pady=5)

    def __on_key_press(self, event):
        if event.keysym in self.key_labels:
            label = self.key_labels[event.keysym]
            self.__update_key_label(label, pressed=True)
            self.pressed_keys.add(event.keysym)
            ctrl.pressed_keys_handler(self.pressed_keys)
        else:
            pressed_char = event.char.upper()
            if pressed_char in self.key_labels:
                label = self.key_labels[pressed_char]
                self.__update_key_label(label, pressed=True)
                self.pressed_keys.add(pressed_char)
                ctrl.pressed_keys_handler(self.pressed_keys)

    def __on_key_release(self, event):
        if event.keysym in self.key_labels:
            label = self.key_labels[event.keysym]
            self.__update_key_label(label, pressed=False)
            self.pressed_keys.remove(event.keysym)
        else:
            pressed_char = event.char.upper()
            if pressed_char in self.key_labels:
                label = self.key_labels[pressed_char]
                self.__update_key_label(label, pressed=False)
                self.pressed_keys.remove(pressed_char)


def make_button_label(key, parent):
    return tk.Label(
        parent, text=key, font=("Arial", 16, "bold"), fg="white", bg="#555555",
        width=4, height=2, relief="raised", borderwidth=2
    )

if __name__ == "__main__":
    app = MainView()
    app.mainloop()
