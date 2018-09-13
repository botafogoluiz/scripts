#-*-coding: utf-8 -*-
from sikuli import *

def paridade():
    wait(2)
    click(Pattern("1535664023862.png").similar(0.92))
    wait(2)
    click(Pattern("1535715873170.png").targetOffset(-50,-19))
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.RIGHT)
    type(Key.RIGHT)
    wait(2)
     # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.RIGHT)
    type(Key.DOWN)
    type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(2)
    click("1535130988948.png")
    wait(2)
    click(Pattern("1535716255453.png").targetOffset(150,-52))
    wait(2)
    type(Key.DOWN)
    wait(1)
    type(Key.DOWN)
    wait(2)
    type("v",KEY_CTRL)
    wait(2)
    print("Quadro tarifario pronto")
    click("1535659828420.png")
    
def main():
    paridade()
    
if __name__ == "__main__":
    main() 