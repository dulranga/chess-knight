class Row:
    MAX_NUM_ROWS = 8

    def __init__(self, row: int):
        self.row = row

    def next_row(self):
        if self.row + 1 > self.MAX_NUM_ROWS:
            return None
        return self.row + 1

    def previous_row(self):
        if self.row <= 0:
            return None

        return self.row - 1

    def move_row_by_count(self, count: int):
        new_row = self.row + count
        if new_row > self.MAX_NUM_ROWS:
            return None
        if new_row <= 0:
            return None
        return Row(new_row)
