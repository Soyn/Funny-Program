#-*- coding:utf-8-*-
__author__ = 'dell'

import turtle
from  Tkinter import *
from random import *

BranchLength = 75
Step = 5
def createGUI(Step = 5, BranchLength = 75):
    TreeControl = Tk()
    TreeControl.title("Awesome-Tree")
    Label(TreeControl, text = "Step").grid(row = 0, column = 0)
    Entry1 = Entry(TreeControl)
    Entry1.grid(row = 0, column = 1)
    Step = Entry1.get()

    Label(TreeControl, text = "TreeLength").grid(row = 2, column = 0)
    Entry2 = Entry(TreeControl)
    Entry2.grid(row = 2, column = 1)
    BranchLength = Entry2.get()


    Button(TreeControl, text = "Draw A Tree", command = Draw).grid(row = 1, column = 2, rowspan = 3)
    TreeControl.mainloop()

def tree(branchLen, t):
    t.pencolor((random(), random(), random()))
    if branchLen > 5:
        t.forward(branchLen)
        t.right(10)
        tree(branchLen - 15, t)
        t.left(20)
        tree(branchLen - 15, t)
        t.right(10)
        t.backward(branchLen)

def Draw():
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

if __name__ == "__main__":
    createGUI()
