#-*- coding:utf-8-*-
__author__ = 'dell'

import turtle
from random import *
def tree(branchLen, t):
    t.pencolor((random(), random(), random()))
    if branchLen > 5:
        t.forward(branchLen)
        t.right(10)
        tree(branchLen - 5, t)
        t.left(20)
        tree(branchLen - 5, t)
        t.right(10)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(10)
    t.speed(0)
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t)
    myWin.exitonclick()

main()

