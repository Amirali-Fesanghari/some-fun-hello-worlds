import os , sys , time 
from random import uniform
from colorama import Fore, Back, Style


def printing_hello_world(text ,rate, r,g,b):
    speeds = [rate-0.08, rate+0.08]
    for index in text:
        print(Style.BRIGHT + Fore.YELLOW + Back.BLUE + index ,end="", flush=True)
        time.sleep(uniform(speeds[0],speeds[1]))

printing_hello_world("Hello",0.45,0,255,0)
