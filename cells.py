from tkinter import Button
from random import sample
import ctypes
import sys

class Cell:
    elements = []
    def __init__(self,X,Y, mine=False):
        self.mine = mine
        self.cell_button_object = None
        self.X = X
        self.Y = Y
        
        Cell.elements.append(self)

    def create_button(self, location):
        btn = Button(location,height = 4, width = 13)
        self.cell_button_object = btn
        btn.bind('<Button-1>',self.left_action )
        btn.bind('<Button-3>',self.right_action )

    def left_action(self, event):
        if self.mine:
            self.display_mine()
        else:
            if self.surrounding_mine_counter == 0:
                for i in self.surrounded_cells:
                    i.display_cell() 
            self.display_cell()

    def right_action(self, event):
        self.cell_button_object.configure(text = "🚩")
    
    def display_mine(self):
        self.cell_button_object.configure(text="💣")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "game Over", 0)
        sys.exit()

    @property
    def surrounded_cells(self):
        nearby_cells = [
            self.display_axis(self.X - 1, self.Y - 1), self.display_axis(self.X - 1, self.Y), self.display_axis(self.X - 1, self.Y + 1),
            self.display_axis(self.X, self.Y - 1), self.display_axis(self.X + 1, self.Y - 1), self.display_axis(self.X + 1, self.Y), self.display_axis(self.X + 1, self.Y + 1),
            self.display_axis(self.X, self.Y + 1) ]
        surrounding_cells = []
        for i in nearby_cells:
            if i != None:
                surrounding_cells.append(i)
        return surrounding_cells

    @property
    def surrounding_mine_counter(self):
        count = 0
        for i in self.surrounded_cells:
            if i.mine:
                count += 1
        return count

    def display_cell(self):
        self.cell_button_object.configure(text = self.surrounding_mine_counter)

            
                

    def display_axis(self, X, Y):
        for cell in Cell.elements:
            if cell.X == X and cell.Y == Y:
                return cell




    @staticmethod
    def random_mines():
        mine_cells = sample(Cell.elements, 9)
        
        for mines in mine_cells:
            mines.mine = True   


