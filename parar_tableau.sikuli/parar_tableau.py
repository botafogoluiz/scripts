#-*-coding: utf-8 -*-
from sikuli import *
#Parar a exibição do Tableau
def parar_tableau():
    wait(5)
    type(Key.F11)
    wait(5)
    click("1534343161403.png")
    wait(5)
    click("1534343235897.png")
    wait(2)
    print "Tableau parado corretamente"
def main():
    parar_tableau()
if __name__ == "__main__":
    main()