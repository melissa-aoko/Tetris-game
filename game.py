from grid import Grid
from blocks import *
import random
import json
from block import Block

SAVE_FILE = "save.json"

class Game:
    def __init__(self):
        self.grid= Grid()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block =self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over=False
        self.score=0

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared==1:
            self.score +=100
        elif lines_cleared==2:
            self.score +=300
        elif lines_cleared==3:
            self.score +=500
        self.score += move_down_points


    def get_random_block(self):
        if len(self.blocks)==0:
          self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
  
        block= random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0,-1)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(0,1)

    def move_right(self):
        self.current_block.move(0,1)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(0,-1)
        
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.move(-1,0)
            self.lock_block()

    def lock_block(self):
        tiles= self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column]=self.current_block.id
        self.current_block=self.next_block
        self.next_block=self.get_random_block()
        rows_cleared=self.grid.clear_full_rows()
        self.update_score(rows_cleared,0)
        if self.block_fits()==False:
            self.game_over=True

    def reset(self):
        self.grid.reset()
        self.blocks= [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.score=0


    def block_fits(self):
        tiles =self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column)==False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()

        if self.block_inside()==False or self.block_fits()==False:
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles= self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column)==False:
                return False
        return True
    
    
    def save_game_state(self, username):
        state = {
            "score": self.score,
            "grid": self.grid.grid,
            "current_block": self.current_block.to_dict(),
            "next_block": self.next_block.to_dict()
        }
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
        except:
            data = {}

        data[username] = state

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    def load_game_state(self, username):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)

            if username in data:
                state = data[username]
                self.score = state["score"]
                self.grid.grid = state["grid"]
                self.current_block = Block.from_dict(state["current_block"])
                self.next_block = Block.from_dict(state["next_block"])
                
        except Exception as e:
            print("Failed to load saved game:", e)

    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11,11)

        if self.next_block.id==3:
            self.next_block.draw(screen, 255,290)
        elif self.next_block.id==4:
            self.next_block.draw(screen,255,280)
        else:
            self.next_block.draw(screen, 270, 270)

       