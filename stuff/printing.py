#Patrick Fennell z5218631
#base for functions for printing

import time

def Greenprint(words):
    print("\033[31;1;4m" + words + "\033[0m")

def PrintTitle():
    print("    _                   _ _                              __                _   ")
    print("   /_\\    ____ __  __ _| | |  ____ _  _____ __ ___  _   / _|___ _ _ ___ __| |_ ")
    print("  / _ \\  (_-< '  \\/ _` | | | (_-< ' \\/ _ \\ V  V / || | |  _/ _ \\ '_/ -_|_-<  _|")
    print(" /_/ \\_\\ /__/_|_|_\\__,_|_|_| /__/_||_\\___/\\_/\\_/ \\_, | |_| \\___/_| \\___/__/\\__|")
    print("                                                 |__/                          ")
    print(" ")

def Print(words):
    time.sleep(0.5)
    print("\033[32m>" + words + "\033[0m")

def PrintOpt(words):
    time.sleep(0.1)
    print("\033[36;1m>" + words + "\033[0m")

def PrintGain(words):
    time.sleep(0.5)
    print("\033[33;1m>" + words + "\033[0m")

def PrintItem(words):
    time.sleep(0.5)
    print("\033[35;1m>  " + words + "\033[0m")

def PrintHitByPlayer(words):
    time.sleep(0.5)
    print("\033[32;1m>  " + words + "\033[0m")

def PrintHitByPlayerCrit(words):
    time.sleep(0.5)
    print(">  \033[32;1;3;4m" + words + "\033[0m")

def PrintHitByEnemy(words):
    time.sleep(0.5)
    print("\033[31;1m>  " + words + "\033[0m")

def PrintHitByEnemyCrit(words):
    time.sleep(0.5)
    print(">  \033[32;1;3;4m" + words + "\033[0m")



        