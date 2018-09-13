#-*-coding: utf-8 -*-
from sikuli import *

def investimento():
    wait(2)
    click()
    click(Pattern("1536070068971.png").targetOffset(2,23))
    wait(2)
    type(Key.DOWN)
    wait(2)
    type("c",KEY_CTRL)
    wait(1)
    click("1536070379132.png")
    wait(2)
    click("1536070433996.png")
    type(Key.DOWN)
    wait(2)
    type("v",KEY_CTRL)
    wait(2)
    click("1536070575832.png")
    wait(2)
    click("1536070642607.png")
    type(Key.RIGHT)
     # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1536070848295.png")
    wait(2)
    click("1536070874467.png")
    type(Key.RIGHT)
    wait(1)
    type("v",KEY_CTRL)
    wait(2)
    click("1536070575832.png")
    wait(2)
    click("1536071702742.png")
    wait(2)
    type(Key.RIGHT)
    type(Key.RIGHT)
    type(Key.DOWN)
    type(Key.DOWN)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    for i in range (0,38):
        type(Key.DOWN)
    type(Key.RIGHT)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1536070848295.png")
    wait(2)
    click(Pattern("1536071952899.png").targetOffset(52,11))
    wait(2)
    type("v",KEY_CTRL)
    wait(80) #trocar para 80
    click("1536157702104.png")
    
def main():
    investimento()
          
if __name__ == "__main__":
    main() 