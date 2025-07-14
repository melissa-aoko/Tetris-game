from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		self.id = id
		self.cells = {}
		self.cell_size = 30
		self.row_offset = 0
		self.column_offset = 0
		self.rotation_state = 0
		self.position = Position(0, 4)
		self.colors = Colors.get_cell_colors()

	def to_dict(self):
			return {
				"id": self.id,
				"rotation_state": self.rotation_state,
				"position": [self.position.row, self.position.column],
				
			}

	@classmethod
	def from_dict(cls, data):
			from blocks import LBlock, JBlock, IBlock, OBlock, SBlock, TBlock, ZBlock

			block_map = {
				1: LBlock,
				2: JBlock,
				3: IBlock,
				4: OBlock,
				5: SBlock,
				6: TBlock,
				7: ZBlock,
			}
			block_id = data.get("id")
			block_class = block_map.get(block_id, Block)
			block = block_class()

			# Default to 0 if rotation_state key is missing
			block.rotation_state = data.get("rotation_state", 0)

			# Default to [0, 4] if position key is missing
			pos = data.get("position", [0, 4])
			block.position = Position(*pos)

			return block

	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns

	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0

	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)


