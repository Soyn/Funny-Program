#-*- coding:utf8-*-
__author__ = 'dell'


from Tkinter import *
from random import *
import turtle

class DrawATree(object):
    def __int__(self, BranchLength, Step):
        self.BranchLength = BranchLength
        self.Step = Step


    def GetText(self,str1, str2):
        self.Step = str1.get()
        self.BranchLength = str2.get()


    def CreateGUI(self):
        TreeControl = Tk()
        TreeControl.title("Awesome-Tree")
        Label(TreeControl, text = "Step").grid(row = 0, column = 0)
        Label(TreeControl, text = "TreeLength").grid(row = 2, column = 0)
        Entry1 = Entry(TreeControl)
        Entry1.grid(row = 0, column = 1)
        Entry2 = Entry(TreeControl)
        Entry2.grid(row = 2, column = 1)
        self.GetText(Entry1,Entry2)
        Button(TreeControl, text = "Draw A Tree", command = self.show_Entry).grid(row = 1, column = 2, rowspan = 3)
        TreeControl.mainloop()



    def tree(self, t):
        t.pencolor((random(), random(), random()))
        BL = self.BranchLength
        ST = self.Step
        if BL > 5:
            t.forward(BL)
            t.right(10)
            tree(BL -ST, t)
            t.left(20)
            tree(BL - ST, t)
            t.right(10)
            t.backward(BL)

    def show_Entry(self):
        print "BranchLength:%s\nStep:%s" %(self.BranchLength, self.Step)

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
    root = DrawATree()
    root.CreateGUI()
