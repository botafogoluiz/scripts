#-*-coding: utf-8 -*-
from sikuli import *

def tarifa_especial():
    wait(2)
    click("1535996663555.png")
    wait(2)
    click("1535992107194.png")
    wait(2)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.RIGHT)
    type(Key.RIGHT)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    for i in range (0,302):
        type(Key.DOWN)
    for i in range (0,11):
        type(Key.RIGHT)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    click("1535994487533.png")
    wait(2)
    click("1535995582893.png")
    wait(2)
    click(Pattern("1535995636230.png").targetOffset(160,-2))
    type("v",KEY_CTRL)
    wait(15)
    click("1535996586384.png")
    print("Tarifa Especial Pronta")

def main():
    tarifa_especial()
        
if __name__ == "__main__":
    main()