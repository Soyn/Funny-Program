#-*- coding:utf8-*-
__author__ = 'dell'


from Tkinter import *
from random import *
import turtle

class DrawATree(object):
    def __int__(self, BranchLength, Step):
        self.BranchLength = BranchLength
        self.Step = Step


    def CreateGUI(self):
        TreeControl = Tk()
        TreeControl.title("Awesome-Tree")
        Label(TreeControl, text = "Step(5~20)").grid(row = 0, column = 0)
        Label(TreeControl, text = "TreeLength(75~100)").grid(row = 2, column = 0)
        Label(TreeControl, text = "PenSize(1~10)").grid(row = 3, column = 0)
        Entry1 = Entry(TreeControl)
        Entry1.grid(row = 0, column = 1)
        Entry2 = Entry(TreeControl)
        Entry2.grid(row = 2, column = 1)
        Entry3 = Entry(TreeControl)
        Entry3.grid(row = 3, column = 1)
        Button(TreeControl, text = "Quit", command = TreeControl.quit).grid(row = 2, column = 2)
        Button(TreeControl, text = "Draw A Tree", command = lambda e1 = Entry1, e2 = Entry2, e3 = Entry3: self.Draw(e1, e2,e3)).grid(row = 3, column = 2, rowspan = 3)
        Button(TreeControl, text = "Save Picture", command = self.SaveScreenShot).grid(row = 1, column = 2)
        TreeControl.mainloop()

    def SaveScreenShot(self):
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file = "screenshot.png")



    def tree(self,bl, t):
        t.pencolor((random(), random(), random()))
        BL = bl
        ST = self.Step
        if BL > 5:
            t.forward(BL)
            t.right(10)
            self.tree(BL -ST, t)
            t.left(20)
            self.tree(BL - ST, t)
            t.right(10)
            t.backward(BL)

    def show_Entry(self):
        print "BranchLength:%s\nStep:%s" %(self.BranchLength, self.Step)

    def Draw(self, e1, e2,e3):
        self.Step = eval(e1.get())
        self.BranchLength = eval(e2.get())
        pensize = eval(e3.get())
        t = turtle.Turtle()
        t.hideturtle()
        t.pensize(pensize)
        t.speed(0)
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        self.tree(self.BranchLength,t)
        myWin.exitonclick()


if __name__ == "__main__":
    root = DrawATree()
    root.CreateGUI()
