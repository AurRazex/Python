import time
import time
import random
import pyfiglet as pf
from pyfiglet import Figlet
from termcolor import colored


Text = "I Love You"

Name = "Evgenia"


reverseText = Name[::-1]

colorList = ['red', 'green', 'yellow', 'blue']
timeInterval = [0.2, 0.3, 0.2, 0.4]


dataList = list()
with open('Fonts.txt') as f:
    for line in f:
        dataList.append(line.strip())

for i in range(1,1000):
    if(i%10==0):
        textArt = pf.figlet_format(Text)
        print("\n", textArt)
    elif(i%9 == 0):
        textArt = pf.figlet_format(Text, font="xsbook")
        print(textArt)
    elif(i%5==0):
        F = Figlet(font=random.choice(dataList))
        textArt = colored(F.renderText(Name), random.choice(colorList))
        print("\n", textArt)
    elif(i%8==0):
        F = Figlet(font=random.choice(dataList))
        textArt = colored(F.renderText(Text), random.choice(colorList))
        print("\n", textArt)
    elif(i%7==0):
        textArt = pf.figlet_format(Text, font=random.choice(dataList))
        print("\n", textArt)
    elif(i%4==0):
        textArt = pf.figlet_format(reverseText, direction = "right-to-left")
        print("\n", textArt)
    else:
        print("")

    time.sleep(random.choice(timeInterval))

