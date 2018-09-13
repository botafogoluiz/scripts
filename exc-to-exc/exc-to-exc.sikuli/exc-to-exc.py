#-*-coding: utf-8 -*-
from sikuli import *

def volume_faturado():
    wait(2)
    click()
    click("1536172110095.png")
    for i in range (0,10):
        type(Key.DOWN)
    for i in range (0,5):
        type(Key.RIGHT)
    wait(2)
    keyDown(Key.SHIFT)
    for i in range (0,3):
        type(Key.DOWN)
    for i in range (0,11):
        type(Key.RIGHT)
    wait(2)
    keyUp()
    type("c",KEY_CTRL)
    keyDown(Key.ALT)
    type(Key.TAB)
    wait(2)
    keyUp()
    click("1536172110095.png")
    for i in range (0,10):
        type(Key.DOWN)
    for i in range (0,5):
        type(Key.RIGHT)
    wait(2)
    type("v",KEY_CTRL)
    wait(2)
    keyDown(Key.ALT)
    type(Key.TAB)
    wait(2)
    keyUp()
    for i in range (0,5):
        type(Key.DOWN)
    keyDown(Key.SHIFT)
    for i in range (0,3):
        type(Key.DOWN)
    for i in range (0,11):
        type(Key.RIGHT)
    wait(2)
    keyUp()
    type("c",KEY_CTRL)
    wait(2)
    keyDown(Key.ALT)
    type(Key.TAB)
    wait(2)
    keyUp()
    for i in range (0,5):
        type(Key.DOWN)
    wait(2)
    type("v",KEY_CTRL)
    wait(2)
    keyDown(Key.ALT)
    type(Key.TAB)
    wait(2)
    keyUp()
    for i in range (0,5):
        type(Key.DOWN)
    wait(2)
    keyDown(Key.SHIFT)
    for i in range (0,3):
        type(Key.DOWN)
    for i in range (0,11):
        type(Key.RIGHT)
    wait(2)
    keyUp()
    type("c",KEY_CTRL)
    wait(2)
    keyDown(Key.ALT)
    type(Key.TAB)
    wait(2)
    keyUp()
    for i in range (0,5):
        type(Key.DOWN)
    wait(2)
    type("v",KEY_CTRL)
    
def main():
    volume_faturado()
if __name__ == "__main__":
    main()