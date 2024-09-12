import keypad as Keypad
import Display
import time
import constants
import busio
import board

uart = busio.UART(
        board.TX,
        board.RX,
        baudrate=38400,
        bits=7,
        parity=None,
        stop=1,
        receiver_buffer_size=64,
        timeout=0,
    )

def to_pi(message_type, message_tx):
    message_tx1 = bytearray((message_tx), "utf-8")
    ready = True
    while ready:
        display.clear()
        uart.write(message_tx1)
        if message_type == 2:
            ready = False
        else:
            time.sleep(0.5)
            if uart.read(2) == b"TY":
                for i in constants.T_msg:
                    display.write(i)
                time.sleep(5)
                display.clear()
                ready = False
            else:
                for i in constants.E_msg:
                    display.write(i)
                time.sleep(5)

def ent_RA_DEC():
    RA_DEC = ""
    for i in constants.menu[1]:
        display.write(i)
    for i in constants.RA_DEC_temp:
        if i == "0":
            x = Keypad.get(False)
            while x not in constants.set5:
                x = Keypad.get(False)
            display.write(x)
            RA_DEC = RA_DEC + x
        elif i == "?":
            x = 0
            while x not in ("+", "-"):
                x = Keypad.get(False)
                if x == "A":
                    x = "+"
                    display.write(x)
                    RA_DEC = RA_DEC + x
                elif x == "B":
                    x = "-"
                    display.write(x)
                    RA_DEC = RA_DEC + x
        elif i == "v":
            x = Keypad.get(False)
            while x not in constants.set1:
                x = Keypad.get(False)
            display.write(x)
            RA_DEC = RA_DEC + x
        elif i == "w":
            x = Keypad.get(False)
            while (x not in constants.set2) and (RA_DEC[0] == "2"):
                x = Keypad.get(False)
            display.write(x)
            RA_DEC = RA_DEC + x
        elif (i == "x") or (i == "z"):
            x = Keypad.get(False)
            while x not in constants.set3:
                x = Keypad.get(False)
            display.write(x)
            RA_DEC = RA_DEC + x
        elif i == "y":
            x = Keypad.get(False)
            while x not in constants.set4:
                x = Keypad.get(False)
            display.write(x)
            RA_DEC = RA_DEC + x
        else:
            display.write(i)
            RA_DEC = RA_DEC + i
    to_pi(1, ("START" + RA_DEC + "END"))
    for i in constants.Track:
        display.write(i)
    x = Keypad.get(False)
    while x != "B":
        if x == "A":
            to_pi(2, constants.Track_msg)
        else:
            to_pi(2, constants.STOP)
        for i in "Tracking...":
            display.write(i)
            time.sleep(0.5)
        display.clear()
        x = Keypad.jog("A")
    to_pi(5, constants.STOP_TRACK)

def jog():
    jogging = True
    while jogging:
        x = Keypad.get(True)
        if x == "2":
            while x == "2":
                print("up")
                to_pi(2, constants.UP)
                x = Keypad.jog(x)
            to_pi(2, constants.STOP)
        elif x == "8":
            while x == "8":
                print("down")
                to_pi(2, constants.DOWN)
                x = Keypad.jog(x)
            to_pi(2, constants.STOP)
        elif x == "4":
            while x == "4":
                print("left")
                to_pi(2, constants.LEFT)
                x = Keypad.jog(x)
            to_pi(2, constants.STOP)
        elif x == "6":
            while x == "6":
                print("right")
                to_pi(2, constants.RIGHT)
                x = Keypad.jog(x)
            to_pi(2, constants.STOP)
        elif x == "A":
            print("end")
            to_pi(2, constants.STOP_TRACK)
            jogging = False

def menu():
    y = 0
    for i in constants.menu[0]:
        display.write(i)
    while True:
        x = Keypad.get(False)
        if x == "C" and y > 0:
            y = y - 1
            display.clear()
            for i in constants.menu[y]:
                display.write(i)
        elif x == "C" and y == 0:
            display.clear()
            for i in constants.menu[y]:
                display.write(i)
        elif x == "D" and y < 2:
            y = y + 1
            display.clear()
            for i in constants.menu[y]:
                display.write(i)
        elif x == "D" and y == 2:
            display.clear()
            for i in constants.menu[y]:
                display.write(i)
        elif x == "#" and y > 0:
            display.clear()
            if y == 1:
                to_pi(1, constants.COORDS)
                ent_RA_DEC()
            elif y == 2:
                to_pi(3, constants.JOG)
                jog()


display = Display.display()

while True:
    menu()
