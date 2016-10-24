import explorerhat
from time import sleep

def forwards (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.forward(100)
    sleep(5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def backwards (channel, event):
    explorerhat.motor.one.backward(100)
    explorerhat.motor.two.backward(100)
    sleep(5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def leftTurn (channel, event):
    explorerhat.motor.one.forward(100)
    explorerhat.motor.two.backward(100)
    sleep(5)
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def rightTurn (channel, event):
    explorerhat.motor.two.backward(100)
    explorerhat.motor.one.forward(100)
    sleep(5)
    explorerhat.motor.two.stop()
    explorerhat.motor.one.stop()
    
explorerhat.touch.one.pressed(forwards)
explorerhat.touch.two.pressed(backwards)
explorerhat.touch.three.pressed(leftTurn)
explorerhat.touch.four.pressed(rightTurn)
