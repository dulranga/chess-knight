import string


class Column:
    """All chess board columns"""

    column_index: int

    ALL_COLUMNS = string.ascii_lowercase[:8]

    def __init__(self, column):
        self.column = column
        self.column_index = self.ALL_COLUMNS.find(self.column)

    def next_column(self):

        if self.column_index + 1 >= len(self.ALL_COLUMNS):
            return None

        return self.ALL_COLUMNS[self.column_index + 1]

    def previous_column(self):
        if self.column_index - 1 < 0:
            return None

        return self.ALL_COLUMNS[self.column_index - 1]

    def move_column_by_count(self, count: int):
        if self.column_index + count >= len(self.ALL_COLUMNS):
            return None
        if self.column_index + count < 0:
            return None

        return Column(self.ALL_COLUMNS[self.column_index + count])
