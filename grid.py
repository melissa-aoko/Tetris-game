import pygame


class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30 # size in pixels

        #2d array to represet grids , list of lists
        self.grid =[[0 for j in range(self.num_cols)]for i in range(self.num_rows)]

        self.colors = self.get_cell_colors()

    def print_grid(self):
        for row in range (self.num_rows):
            for column in range (self.num_cols):
                print(self.grid[row][column], end=" ")
            print()


    def get_cell_colors(self):
        dark_grey   = (26, 31, 40)
        cyan        = (163, 216, 244) 
        yellow      = (255, 246, 165)  
        purple      = (217, 184, 255)  
        mint_green  = (182, 245, 216)  
        coral_pink  = (255, 181, 181)  
        peach       = (255, 209, 164)  
        rose        = (255, 183, 227)  

        return [dark_grey,cyan, yellow, purple, mint_green, coral_pink, peach, rose]

    def draw (self, screen):
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect= pygame.Rect(column*self.cell_size +1, row*self.cell_size+1, self.cell_size -1, self.cell_size-1)
                pygame.draw.rect(screen, self.colors[cell_value],cell_rect)
