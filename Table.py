class Table:
    def __init__(self,cols,rows) -> None:
        self.maze = [[0] * cols for _ in range(rows)]
