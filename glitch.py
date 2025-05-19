import random
import sys
import time
import string
from colorama import Fore , Style , Back

chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+ "
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]



def searching_text(text, delay=0.05):
    displayed = [' '] * len(text)
    colored_line = [' '] * len(text)
    finall_text = ' '
    loop = len(text)-1
    
    for i in range(len(text)):
        # print('\r'+ str(i))
        for _ in range(loop):
            displayed[i] = random.choice(chars)
            # print(displayed[i])
            color = random.randint(0, 4)
            colored_line[i] += colors[color] + displayed[i]
            sys.stdout.write('\r'+ colored_line[i] + Style.RESET_ALL)
            # sys.stdout.write(colors[color]+'\r' + ''.join(displayed))
            sys.stdout.flush()
            time.sleep(delay)

        displayed[i] = text[i]
        
        colored_line[i] += colors[color] + displayed[i]
        sys.stdout.write('\r'+ colored_line[i] + Style.RESET_ALL)
        # sys.stdout.write(colors[color]+'\r' + ''.join(displayed))
        sys.stdout.flush()
        time.sleep(delay)
    for i in range(len(text)):
        # print('\r'+ str(i))
        color = random.randint(0, 4)
        finall_text += colors[color] + displayed[i]
        sys.stdout.write('\r'+ finall_text + Style.RESET_ALL)
        # sys.stdout.write(colors[color]+'\r' + ''.join(displayed))
        sys.stdout.flush()
        time.sleep(delay)
    

user_text = str(input(Back.RED+Style.BRIGHT+Fore.LIGHTCYAN_EX+"enter the word to be printed : " +Style.RESET_ALL))
searching_text(user_text)