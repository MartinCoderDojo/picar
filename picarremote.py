import explorerhat
from time import sleep
from tkinter import *

class App:

    def forwards (self):
        explorerhat.motor.one.forward(100)
        explorerhat.motor.two.forward(100)
        sleep(1)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

    def backwards (self):
        explorerhat.motor.two.backward(100)
        explorerhat.motor.one.backward(100)
        sleep(1)
        explorerhat.motor.two.stop()
        explorerhat.motor.one.stop()

    def leftTurn (self):
        explorerhat.motor.one.forward(100)
        explorerhat.motor.two.backward(100)
        sleep(1)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

    def rightTurn (self):
        explorerhat.motor.one.backward(100)
        explorerhat.motor.two.forward(100)
        sleep(1)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        master.title("")
        self.left = Button(frame, 
                             text=u"\u2191", command=self.forwards)
        self.left.pack(side=TOP)
        self.down = Button(frame,
                             text=u"\u2193", command=self.backwards)
        self.down.pack(side=BOTTOM)
        self.left = Button(frame,
                             text=u"\u2190", command=self.leftTurn)
        self.left.pack(side=LEFT)
        self.right = Button(frame,
                             text=u"\u2192", command=self.rightTurn)
        self.right.pack(side=RIGHT)


root = Tk()
app = App(root)
root.mainloop()
    
