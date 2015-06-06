#-*- coding:utf8-*-
__author__ = 'dell'

from  Tkinter import *
import ColorfulTree


class TreeGUI():
    def __init__(self, step = 5, treeLength = 75):
        self.step  = step
        self.treeLength = treeLength

    def createGUI(self):
        TreeControl = Tk()
        TreeControl.title("Awesome-Tree")
        Label(TreeControl, text = "Step").grid(row = 0, column = 0)
        Entry1 = Entry(TreeControl)
        Entry1.grid(row = 0, column = 1)
        self.step = Entry1.get()

        Label(TreeControl, text = "TreeLength").grid(row = 2, column = 0)
        Entry2 = Entry(TreeControl)
        Entry2.grid(row = 2, column = 1)
        self.treeLength = Entry2.get()


        Button(TreeControl, text = "Draw A Tree", command = ColorfulTree.main).grid(row = 1, column = 2, rowspan = 3)
        TreeControl.mainloop()

if __name__ == "__main__":
    Start = TreeGUI().createGUI()



