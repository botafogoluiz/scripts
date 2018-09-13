#-*-coding: utf-8 -*-
from sikuli import *

def substituicao_hds():
    wait(2)
    click("1536154659420.png")
    wait(2)
    click("1536154699840.png")
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.RIGHT)
    type(Key.RIGHT)
    # Copia da primeira coluna
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    for i in range (0,23):
        type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(1)
    hover("1536155168256.png")
    click("1536154871685.png") 
    wait(2)
    click(Pattern("1536155268748.png").targetOffset(288,14))
    wait(2)
    type("v",KEY_CTRL)
    wait(5)
    click("1535661041191.png")
    type(Key.RIGHT)
    for i in range (0,147):
        type(Key.DOWN)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    for i in range (0,24):
        type(Key.DOWN)
    for i in range (0,3):
        type(Key.RIGHT) 
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(2)
    type(Key.RIGHT)
    for i in range (0,148):
        type(Key.DOWN)
        wait(0.5)
    wait(2)
    type("v",KEY_CTRL)
    wait(3)
    print "Substituicao de HDS copiado"
    click("1535661041191.png")

def main():
    substituicao_hds()
          
if __name__ == "__main__":
    main()