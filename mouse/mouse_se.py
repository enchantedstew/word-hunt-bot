import mouse.mouse_emulate as mse
import math
import time


class MouseSE:
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.current_button = 0
        self.dimentions = (640, 1136)
        self.client = mse.MouseClient()
        self.client.state = [0, 128, 128, 0]
        for i in range(20):
            self.client.send_current()

    def raw_move(self, dx, dy):
        self.client.state = [int(self.current_button), dx, dy, 0]
        self.client.send_current()

    def goto(self, x, y):
        x_dif = x - self.current_x
        y_dif = y - self.current_y
        self.client.send_current()
        self.client.state = [int(self.current_button), 0, 0, 0]
        self.client.send_current()
        while x_dif != 0 or y_dif != 0:
            self.client.state = [
                int(self.current_button),
                int(self.calcer(x_dif)),
                0,
                0,
            ]
            self.client.send_current()
            self.client.state = [int(self.current_button), 0, 0, 0]
            self.client.send_current()
            self.client.state = [
                int(self.current_button),
                0,
                int(self.calcer(y_dif)),
                0,
            ]
            self.client.send_current()
            x_dif -= self.capper(x_dif)
            y_dif -= self.capper(y_dif)
            self.client.state = [int(self.current_button), 0, 0, 0]
            self.client.send_current()

        self.current_x = x
        self.current_y = y

    def reset(self):
        self.current_x = 0
        self.current_y = 0
        self.client.state = [0, 128, 128, 0]
        for i in range(20):
            self.client.send_current()

    def calcer(self, value):
        new_val = abs(value)
        new_val = min(10, new_val)

        if value < 0:
            new_val = 256 - new_val
        return new_val

    def press(self, mouse_down):
        if mouse_down:
            self.current_button = 1
        else:
            self.current_button = 0
        self.client.state = [int(self.current_button), 0, 0, 0]
        self.client.send_current()

    def capper(self, value):
        return math.copysign(min(abs(value), 10), value)
