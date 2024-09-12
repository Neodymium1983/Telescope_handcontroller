#constants

menu= (
        "Hello select opt                        ",
        "Enter RA and DEC                        ",
        "Joystick cont                           ",
    )
Track = "Track? A=Y B=N"
RA_DEC_temp = "vwhx0.0m ?y0dz0"
E_msg = "Error - Retrying."
T_msg = "DATA sent."

set1 = ("0", "1", "2")
set2 = ("0", "1", "2", "3")
set3 = ("0", "1", "2", "3", "4", "5")
set4 = ("0", "1", "2", "3", "4", "5", "6", "7", "8")
set5 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")


Track_msg = "STARTtrack END"
STOP_TRACK = "STARTTstop END"
UP = "STARTup END"
RIGHT = "STARTright END"
LEFT = "STARTleft END"
DOWN = "STARTdown END"
STOP = "STARTstop END"
COORDS = "STARTCOORDS END"
JOG = "STARTjog END"


#display constants
D_comm = 0x00   #tells dis command coming
D_write = 0x40
D_on = 0x0C
D_clear = 0x01
D_cursor = 0x0F
D_twoline = 0x3C
D_curL = 0x10   #cursor left
D_curR = 0x14   #cursor right

letters_nums = {
            "A": 0x41,
            "B": 0x42,
            "C": 0x43,
            "D": 0x44,
            "E": 0x45,
            "F": 0x46,
            "G": 0x47,
            "H": 0x48,
            "I": 0x49,
            "J": 0x4A,
            "K": 0x4B,
            "L": 0x4C,
            "M": 0x4D,
            "N": 0x4E,
            "O": 0x4F,
            "P": 0x50,
            "Q": 0x51,
            "R": 0x52,
            "S": 0x53,
            "T": 0x54,
            "U": 0x55,
            "V": 0x56,
            "W": 0x57,
            "X": 0x58,
            "Y": 0x59,
            "Z": 0x5A,
            " ": 0x20,
            "a": 0x61,
            "b": 0x62,
            "c": 0x63,
            "d": 0x64,
            "e": 0x65,
            "f": 0x66,
            "g": 0x67,
            "h": 0x68,
            "i": 0x69,
            "j": 0x6A,
            "k": 0x6B,
            "l": 0x6C,
            "m": 0x6D,
            "n": 0x6E,
            "o": 0x6F,
            "p": 0x70,
            "q": 0x71,
            "r": 0x72,
            "s": 0x73,
            "t": 0x74,
            "u": 0x75,
            "v": 0x76,
            "w": 0x77,
            "x": 0x78,
            "y": 0x79,
            "z": 0x7A,
            "0": 0x30,
            "1": 0x31,
            "2": 0x32,
            "3": 0x33,
            "4": 0x34,
            "5": 0x35,
            "6": 0x36,
            "7": 0x37,
            "8": 0x38,
            "9": 0x39,
            ".": 0x2E,
            "+": 0x2B,
            "-": 0x2D,
            "#": 0x23,
            "*": 0x2A,
            "?": 0x3F,
            "=": 0x3D,
        }
