from view import MainView
from robot import Robot


robot = Robot()

app = MainView(robot)
app.mainloop()
