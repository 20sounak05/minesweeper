from cells import Cell
from tkinter import *
import random





root = Tk()
root.configure(bg="light grey")
root.geometry("800x600") 
root.title("Minesweeper")     

top_frame = Frame(root, bg="black", width=800, height=100)
top_frame.place(x = 0, y = 0)

left_frame = Frame(root, bg="white", width=200, height=600)
left_frame.place(x = 0, y = 75)

icon_frame = Frame(root, bg="cyan", width=200, height=100)
icon_frame.place(x = 0, y = 0)

centr_frame = Frame(root, bg="grey", width=600, height=500)
centr_frame.place(x=200, y=100)


for X in range(6):
    for Y in range(6):
        c1 = Cell(X, Y)
        c1.create_button(centr_frame)
        c1.cell_button_object.grid(column = X, row =Y)


Cell.random_mines()






root.mainloop() #open a window of size given in geometry function and waits for user to close it.
