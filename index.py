from position import Position
from row import Row
from column import Column
import moves

# [currentLocation, destination] = input('Enter location :').strip().split(' ')
current_position, destination = ['d5', 'd6']

current_position = Position(
    Column(current_position[0]),
    Row(int(current_position[1]))
)

destination = Position(
    Column(destination[0]),
    Row(int(destination[1]))
)

possible_moves = moves.get_possible_moves(current_position)
all_possible_moves = moves.get_all_possible_moves(current_position, destination)
