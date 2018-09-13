#-*-coding: utf-8 -*-
from sikuli import *

def cadastro_empresas():
    wait(2)
    click("1535738030517.png")
    wait(1)
    click("1535738109766.png")
    type(Key.DOWN)
    type(Key.DOWN)
    # Push down keys.
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.DOWN)
    # Release keys. 
    keyUp()
    wait(2)
    type("c",KEY_CTRL)
    wait(2)
    click("1535130966422.png")
    wait(2)
    click("1535977650581.png")
    wait(2)
    click(Pattern("1535738353230.png").similar(0.94).targetOffset(7,10))
    wait(2)
    type("v",KEY_CTRL)
    click("1535661041191.png")
    print"Cadastro Empresa Pronto"
    
def main():
    cadastro_empresas()
        
if __name__ == "__main__":
    main()