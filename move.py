import itertools
from typing import List

from position import Position


class Move:
    # (row, column)
    ALL_MOVES = (
        (+2, +1),
        (+1, +2),
        (+2, -1),
        (+1, -2),
        (-2, +1),
        (-1, +2),
        (-1, -2),
        (-2, -1),
    )
    MAX_MOVES_TO_REACH_DESTINATION = 6
    visited_positions:List[Position] = []

    def __init__(self, location: Position, destination: Position):
        self.location = location
        self.destination = destination
        self.visited_positions.append(self.location)



    def get_possible_moves(self):
        possible_moves = []
        for move in self.ALL_MOVES:
            row_movement, column_movement = move

            new_row = self.location.row.move_row_by_count(row_movement)
            new_column = self.location.column.move_column_by_count(column_movement)


            if new_row and new_column:
                new_position = Position(new_column, new_row)
                if new_position not in self.visited_positions:
                    possible_moves.append(new_position)

        return possible_moves

    def find_paths(self):
        if self.location not in self.visited_positions:
            self.visited_positions.append(self.location)

        all_moves = self.get_possible_moves()

        if self.destination in self.visited_positions:
            print()
            print("Found =======", [i.get_position_id() for i in self.visited_positions])
            input()
            return
        else:

            for move in all_moves:
                self.location = move
                self.find_paths()

