from digitalio import DigitalInOut, Direction, Pull
import board
import time


col1 = DigitalInOut(board.D5)
col1.direction = Direction.OUTPUT
col2 = DigitalInOut(board.A5)
col2.direction = Direction.OUTPUT
col3 = DigitalInOut(board.D6)
col3.direction = Direction.OUTPUT
col4 = DigitalInOut(board.D9)
col4.direction = Direction.OUTPUT
row1 = DigitalInOut(board.D10)
row1.direction = Direction.INPUT
row1.pull = Pull.DOWN
row2 = DigitalInOut(board.D11)
row2.direction = Direction.INPUT
row2.pull = Pull.DOWN
row3 = DigitalInOut(board.D12)
row3.direction = Direction.INPUT
row3.pull = Pull.DOWN
row4 = DigitalInOut(board.D13)
row4.direction = Direction.INPUT
row4.pull = Pull.DOWN

def rows(r1, r2, r3, r4, jog):
    if row1.value:
        while row1.value and not jog:
            time.sleep(0.1)
            # print(r1)
        time.sleep(0.1)
        return r1
    elif row2.value:
        while row2.value and not jog:
            time.sleep(0.1)
        time.sleep(0.1)
        return r2
    elif row3.value:
        time.sleep(0.1)
        while row3.value and not jog:
            time.sleep(0.1)
        time.sleep(0.1)
        return r3
    elif row4.value:
        time.sleep(0.1)
        while row4.value and not jog:
            time.sleep(0.1)
        time.sleep(0.1)
        return r4
    else:
        return 10

def get(jog):
    usrin = 10
    while usrin == 10:
        col1.value = True
        usrin = rows("1", "4", "7", "*", jog)
        if usrin != 10:
            return usrin
        while row2.value and jog:
            return usrin
        col1.value = False
        col2.value = True
        usrin = rows("2", "5", "8", "0", jog)
        if usrin != 10:
            return usrin
        if row1.value and jog:
            return (usrin)
        elif row3.value and jog:
            return (usrin)
        col2.value = False
        col3.value = True
        usrin = rows("3", "6", "9", "#", jog)
        if usrin != 10:
            return usrin
        if row2.value and jog:
            return (usrin)
        col3.value = False
        col4.value = True
        usrin = rows("A", "B", "C", "D", jog)
        if usrin != 10:
            return usrin
        col4.value = False


def jog(x):
    if x == "2":
        col2.value = True
        time.sleep(0.01)
        if row1.value == True:
            col2.value = False
            return x
        else:
            col2.value = False
            return "0"
    elif x == "4":
        col1.value = True
        time.sleep(0.01)
        if row2.value == True:
            col1.value = False
            return x
        else:
            col1.value = False
            return "0"
    elif x == "6":
        col3.value = True
        time.sleep(0.01)
        if row2.value == True:
            col3.value = False
            return x
        else:
            col3.value = False
            return "0"
    elif x == "8":
        col2.value = True
        time.sleep(0.01)
        if row3.value == True:
            col2.value = False
            return x
        else:
            col2.value = False
            return "0"
    elif x == "A":
        col4.value = True
        time.sleep(0.01)
        if row1.value == True:
            col4.value = False
            return x
        elif row2.value == True:
            col4.value = False
            return "B"
        else:
            col4.value = False
            return "0"



