import time

import Tkinter as tk
import serial
# import Image
from PIL import Image, ImageTk
from Tkinter import *

iridium = serial.Serial("/dev/ttyUSB0", 19200, timeout=0)


class App():

    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill=BOTH, expand=YES)
        self.button = Button(frame,
                             text="QUIT", fg="red",
                             command=frame.quit)
        self.button.pack(side=BOTTOM, anchor=W, fill=X, expand=YES)

        # Test AT command
        self.SBD = Button(frame,
                          text="AT Ping",
                          command=self.ping)
        self.SBD.pack(side=TOP, anchor=W, fill=X, expand=YES)

        # Check Signal Strength
        self.SBD = Button(frame,
                          text="Check Signal Strength",
                          command=self.signal_strength)
        self.SBD.pack(side=TOP, anchor=W, fill=X, expand=YES)

    # PING FUNCTION - AT&K0
    def ping(self):
        print ("\nCommand Sent. Awaiting Response\n")
        command = "AT"
        iridium.write(command + "\r\n")
        # i=0
        while (True):
            time.sleep(0.5)
            _read_line = iridium.readline().strip()
            if (_read_line != ""):
                _information = _read_line
                print (_information)
            if (_read_line == "ERROR"):
                iridium.flush()
                print("ERROR in Response. Try Again\n")
                break
            if (_read_line == "OK"):
                iridium.flush()
                print("Response Received Successfully\n")
                break

    # SIGNAL STRENGTH REQUEST
    def signal_strength(self):
        print ("\nCommand Sent. Awaiting Response\n")
        command = "AT+CSQ"
        iridium.write(command + "\r\n")
        print ("Awaiting for Signal Strength Response")
        time.sleep(0.5)
        # i=0
        while (True):
            time.sleep(0.1)
            _read_line = iridium.readline().strip()

            if (_read_line != ""):
                _information = _read_line
                print (_information)
            if (_read_line == "ERROR"):
                iridium.flush()
                print("ERROR in Response. Try Again\n")
                break
            if (_read_line == "OK"):
                iridium.flush()
                print("Response Received Successfully\n")
                break
        extra_read_line = iridium.readline().strip()
        print (extra_read_line + "\n")  # Blanc??

    # POWER DOWN IRIDIUM
    def turn_off(self):
        print ("\nCommand Sent. Awaiting Response\n")
        command = "AT*F"
        iridium.write(command + "\r")
        print ("Turn off the device now")
        print("\n")
        iridium.flush()


root = Tk()
ment = StringVar()
root.title("Hackathlon")
root.geometry("600x400")
imageFile = "sac.png"
image1 = ImageTk.PhotoImage(Image.open(imageFile))
image2 = ImageTk.PhotoImage(Image.open("sac.png"))
panel1 = tk.Label(root, image=image1)
display = image1
panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
app = App(root)
root.mainloop()
