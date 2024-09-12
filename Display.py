import busio
from time import sleep
import board
import constants


class display:

    def __init__(self):
        self.disdrvadd = 0x7C >> 1
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
        sleep(0.1)
        self.on()
        self.clear()
        self.twolines()
        self.curser()

    def on(self):
        while not self.i2c.try_lock():  # takes control of i2c
            pass
        sleep(0.01)  # short break
        self.comm = [constants.D_comm, constants.D_on]
        self.command = bytearray(self.comm)
        self.i2c.writeto(self.disdrvadd, self.command)
        self.i2c.unlock()

    def clear(self):
        while not self.i2c.try_lock():
            pass
        sleep(0.01)
        self.comm = [constants.D_comm, constants.D_clear]
        self.command = bytearray(self.comm)
        self.i2c.writeto(self.disdrvadd, self.command)
        self.i2c.unlock()

    def twolines(self):
        while not self.i2c.try_lock():
            pass
        sleep(0.01)
        self.comm = [constants.D_comm, constants.D_twoline]
        self.command = bytearray(self.comm)
        self.i2c.writeto(self.disdrvadd, self.command)
        self.i2c.unlock()

    def curser(self):
        while not self.i2c.try_lock():
            pass
        sleep(0.01)
        self.comm = [constants.D_comm, constants.D_cursor]
        self.command = bytearray(self.comm)
        self.i2c.writeto(self.disdrvadd, self.command)
        self.i2c.unlock()

    def write(self, x):
        while not self.i2c.try_lock():
            pass
        sleep(0.01)
        self.comm = [constants.D_write, constants.letters_nums[x]]
        self.command = bytearray(self.comm)
        self.i2c.writeto(self.disdrvadd, self.command)
        self.i2c.unlock()

