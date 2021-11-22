from typing import List

from position import Position

# (row, column)
ALL_MOVES = (
    (-2, -1),
    (-2, +1),
    (+2, -1),
    (+2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2)
)
MAX_MOVES_TO_REACH_DEST = 6


def get_possible_moves(
        position: Position
) -> List[Position]:
    possible_moves = []

    for move in ALL_MOVES:
        row_movement, column_movement = move

        new_row = position.row.move_row_by_count(row_movement)
        new_column = position.column.move_column_by_count(
            column_movement)

        if new_row and new_column:
            possible_moves.append(Position(new_column, new_row))

    return possible_moves


moved_positions: List[Position] = []


def get_all_possible_moves(
        current_position: Position,
        destination: Position,
        previous_position: Position = None,
        node_level=1
):
    moved_positions.append(current_position)
    print('\n[START BLOCK]')
    print(f'\n[LEVEL IS {node_level}]')
    # input()
    moves = get_possible_moves(current_position)
    print("current_position", current_position.get_position_id())
    print('possible moves', [i.get_position_id() for i in moves])
    print('previous moves', [i.get_position_id() for i in moved_positions])

    if destination in moves:
        print("Found it !!!!")
        input()
        return moved_positions
    else:
        for move in moves:
            print(f"index of this move [{moves.index(move)}] ===> {[i.get_position_id() for i in moves]}", )

            print('to move', move.get_position_id())
            print("previous_position", previous_position and previous_position.get_position_id())

            if move not in moved_positions:
                if not previous_position:
                    print('moved to 1', move.get_position_id())
                    get_all_possible_moves(move, destination, current_position, node_level + 1)

                elif previous_position != move:
                    print('moved to 2', move.get_position_id())
                    get_all_possible_moves(move, destination, current_position, node_level + 1)
            else:
                print('index', moves.index(move), "length", len(moves))
                if moves.index(move) == len(moves): # no moves to go
                    moved_positions.pop()

                print("Cannot go further ===")
                print('modified moves', [i.get_position_id() for i in moved_positions])
                print()
                print()





def get_path_to_destination(current_position: Position, destination: Position):
    yield []
