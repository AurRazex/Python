import math
import sys
import turtle
import time
import time
import random
import pyfiglet as pf
from pyfiglet import Figlet
from termcolor import colored

i = 50



Text = "I Love You"

Name = "Evgenia"


reverseText = Name[::-1]

colorList = ['red', 'green', 'yellow', 'blue']
timeInterval = [0.2, 0.3, 0.2, 0.4]


dataList = []
with open('fonts.txt') as f:
    dataList.extend(line.strip() for line in f)
for i in range(1,100):
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
    

def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * \
math.cos(2 * t) - 2 * \
math.cos(3 * t) -  \
math.cos(4 * t)

t = turtle.Turtle()
t.speed(1000000)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255-i) % 255, i % 255, (255 + i) // 2 % 255)
    t.goto(0, 0)
t.hideturtle()
turtle.update()
turtle.mainloop()