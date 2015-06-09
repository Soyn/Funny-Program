#-*- coding:utf8-*-
__author__ = 'dell'


from Tkinter import *
from random import *
import turtle

class DrawATree():
    def __int__(self, BranchLength = 75, Step = 5):
        self.BranchLength = BranchLength
        self.Step = Step

    def createGUI(self):
        TreeControl = Tk()
        TreeControl.title("Awesome-Tree")
        Label(TreeControl, text = "Step").grid(row = 0, column = 0)
        e = StringVar()
        Entry1 = Entry(TreeControl, textvariable  = e)
        Entry1.grid(row = 0, column = 1)
        self.Step = e.get()

        Label(TreeControl, text = "TreeLength").grid(row = 2, column = 0)
        t = StringVar()
        Entry2 = Entry(TreeControl, textvariable = t)
        Entry2.grid(row = 2, column = 1)
        self.BranchLength = t.get()


        Button(TreeControl, text = "Draw A Tree", command = self.Draw).grid(row = 1, column = 2, rowspan = 3)
        TreeControl.mainloop()

    def tree(self, t):
        t.pencolor((random(), random(), random()))
        if self.BranchLength > 5:
            print self.BranchLength
            t.forward(self.BranchLength)
            t.right(10)
            tree(self.BranchLength - self.Step, t)
            t.left(20)
            tree(self.BranchLength - self.Step, t)
            t.right(10)
            t.backward(self.BranchLength)

    def Draw(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(10)
        t.speed(0)
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        self.tree(t)
        myWin.exitonclick()


if __name__ == "__main__":
    root = DrawATree().createGUI()