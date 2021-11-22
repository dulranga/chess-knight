from column import Column
from row import Row


class Position:
    def __init__(self, column: Column, row: Row):
        self.position = (column, row)
        self.column = column
        self.row = row

    def __eq__(self, other):
        return self.row.row == other.row.row and \
               self.column.column == other.column.column

    def get_position_values(self):
        return (self.column.column, self.row.row)

    def get_position_id(self):
        return f"{self.column.column}{self.row.row}"
