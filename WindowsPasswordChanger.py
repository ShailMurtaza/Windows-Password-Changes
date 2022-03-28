# 13 March, 2020
import sys
import getpass
import os
import crayons
import ctypes
import hashlib
import binascii

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]


font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 15
font.dwFontSize.Y = 15
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    handle, ctypes.c_long(False), ctypes.pointer(font))
userrr = os.environ.get("USERNAME")


def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(unicode, argv[1:])
    else:
        arguments = map(unicode, argv)
    argument_line = u' '.join(arguments)
    executable = unicode(sys.executable)
    if debug:
        print 'Command line: ', executable, argument_line
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None


if __name__ == '__main__':
    ret = run_as_admin()
    if ret is True:
        os.system("title (gamer) Windows password changer HA HA HA !")
        print('------------------------------------------------')
        print("Windows password changer Created by Shail")
        print("------------------------------------------------")
        print("")
        print crayons.red(
            "NOTE :: This software is only for educational and fun purposes.Please don't use it for your bad purposes.", bold=True)
        print crayons.red(
            "IF you do any thing bad with this then I will not be answerable.", bold=True)
        print crayons.red("Test it only on your computer.HAHAHA", bold=True)
        print("")
        passw = getpass.getpass("Enter password for use of SOFTWARE:: ")
        hash = hashlib.new('md4', passw.encode('utf-16le')).digest()
        winner = binascii.hexlify(hash)
        if winner == "d44f2a4a5ca95299bbec456ed02597cf":
            def shail():
                print crayons.blue("Changing password for USERNAME :: " + userrr, bold=True)
                pass1 = getpass.getpass("Enter password for USER: ")
                pass2 = getpass.getpass("conform password: ")
                if pass1 == pass2:
                    os.system("color 0a")
                    change = ("net user " + userrr + " " + pass2)
                    print(change)
                    os.system(str(change))
                    raw_input("")
                else:
                    os.system("color 0c")
                    print("------->> Matching failed !!! PLEASE TRY AGAIN <<-------")
                    raw_input("")
                    shail()
            shail()
        else:
            os.system("color 0b")
            print("INCORrECT PASSWORD HA ha !")
            raw_input("")

    elif ret is None:
        print 'ha'
    else:
        print 'Error(ret=%d): cannot elevate privilege.' % (ret, )
