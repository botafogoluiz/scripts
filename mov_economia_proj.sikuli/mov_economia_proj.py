#-*-coding: utf-8 -*-
from sikuli import *

def mov_economia_proj():
    wait(2)
    click("1536080489631.png")
    wait(2)
    click("1536080668660.png")
    wait(2)
    #parte 1
    for i in range (0,5):
        type(Key.DOWN)
    type(Key.RIGHT)
    type(Key.RIGHT)
      # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.RIGHT)
    type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(2)
    click("1535649880861.png")
    wait(2)
    click(Pattern("1535649951821.png").targetOffset(280,-30))
    wait(2)
    type("v",KEY_CTRL)
    wait(2)
    #parte 2 (Vai repetir 11 vezes, para preencher até Agua Industrial CPH)
    for i in range (0,11):
        click("1535650505796.png")
        for i in range (0,7):
            type(Key.DOWN)
        # Push down keys.
        keyDown(Key.CTRL)
        keyDown(Key.SHIFT)
        type(Key.RIGHT)
        type(Key.DOWN)
        # Release keys. 
        keyUp()
        wait(2)
        type("c",KEY_CTRL)
        wait(2)
        click("1535130966422.png")
        wait(2)
        for i in range (0,7):
            type(Key.DOWN)
            wait(1)
        type("v",KEY_CTRL)
        wait(2)
    print "Fim do loop da agua, gracas a Deus!"
    #parte 1 (Esgoto)
    click("1535650505796.png")
    for i in range (0,10):
        type(Key.DOWN)
        wait(1)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.RIGHT)
    type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(2)
    for i in range (0,10):
        type(Key.DOWN)
        wait(1)
    type("v",KEY_CTRL)
    wait(2)
    #parte 2 esgoto (vai colar até o ultimo item de esgoto)
    for i in range (0,11):
        click("1535650505796.png")
        for i in range (0,7):
            type(Key.DOWN)
        # Push down keys.
        keyDown(Key.CTRL)
        keyDown(Key.SHIFT)
        type(Key.RIGHT)
        type(Key.DOWN)
        # Release keys. 
        keyUp()
        wait(2)
        type("c",KEY_CTRL)
        wait(2)
        click("1535130966422.png")
        wait(2)
        for i in range (0,7):
            type(Key.DOWN)
            wait(1)
        type("v",KEY_CTRL)
        wait(2)
    print "Fim do loop do esgoto, Amem!"
    click("1535659965045.png")
    


def main():
    mov_economia_proj()
          
if __name__ == "__main__":
    main() 