#-*-coding: utf-8 -*-
from sikuli import *

def custos_despesas():
    wait(2)
    click(Pattern("1535997775327.png").targetOffset(-4,5))
    wait(2)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    for i in range (0,14):
        type(Key.RIGHT)
    wait(2)
    # Push down keys.
    keyDown(Key.SHIFT)
    for i in range(0,6):
        type(Key.RIGHT)
    wait(1)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    for i in range(0,28):
        type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    #wait(2)
    #click("1535998622776.png")
    #wait(2)
    #for i in range (0,5):
    #    type(Key.PAGE_UP)
       
    #click(Pattern("1535999391779.png").targetOffset(163,18))
    #wait(2)
    #type("v",KEY_CTRL)
    #wait(4)


def main():
    custos_despesas()
      
    
if __name__ == "__main__":
    main() 