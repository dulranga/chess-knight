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


def get_possible_moves(
        current_position: Position
) -> List[Position]:
    possible_moves = []

    for move in ALL_MOVES:
        row_movement, column_movement = move

        new_row = current_position.row.move_row_by_count(row_movement)
        new_column = current_position.column.move_column_by_count(
            column_movement)

        if new_row and new_column:
            possible_moves.append(Position(new_column, new_row))

    return possible_moves


all_possible_moves = []


def get_all_possible_moves(
        current_position: Position,
        destination: Position,
        path: List[Position] = []
):
    moves = get_possible_moves(current_position)

    for move in moves:

        print(move.get_position_values())
        possible_moves = get_possible_moves(move)

        if destination in possible_moves:
            print(
                '++++++',
                destination.get_position_values(),
                [i.get_position_values() for i in [*path, move]]
            )
            print("Moves are", ' '.join(
                [i.get_position_id() for i in [*path, move]]
            ))
            return
        else:
            if not move in path:
                get_all_possible_moves(move, destination, [*path, move])

            # if (len(path) > 1 and path[-2] == move):
            #     print('Same move')
            # else:
            # print(
            #     move.get_position_values(),
            #     "=======",
            #     [i.get_position_values() for i in possible_moves]
            # )
            print('path', ([i.get_position_id() for i in [*path, move]]))
