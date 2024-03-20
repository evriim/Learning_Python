"""FIGlet is a program for making large letters out of ordinary text"""
import sys
import random
from pyfiglet import Figlet
figlet= Figlet()
try:
    if len(sys.argv) == 1:
        f = Figlet(font=random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1]=="--font" and sys.argv[2] in figlet.getFonts():
        f = Figlet(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")

text = input("Input: ")
print(f.renderText(text))
