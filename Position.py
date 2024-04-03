class Position:
    def __init__(self) -> None:
        self.leftTurn = {'n': 'w', 'w': 's', 's': 'e', 'e': 'n'}
        self.rightTurn = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
        self.f = 'n'
        self.x = 0
        self.y = 0

    def Place(self,table,x,y,f):
        self.x = x
        self.y = y
        self.f = f[0].lower()
        table.maze[x][y] = 'R'
        
    def TurnLeft(self):
        self.f = self.leftTurn[self.f]

    def TurnRight(self):
        self.f = self.rightTurn[self.f]

    def Move(self,table):
        if self.f == 'n':
            if self.x == 0:
                raise Exception(f"Can't move out of the table: (x->{self.x},y->{self.y},facing->{self.f})")
            else:
                table.maze[self.x][self.y] = 0
                self.x = self.x - 1
                table.maze[self.x][self.y] = 'R'
        elif self.f == 's':
            if self.x == len(table.maze[0]):
                raise Exception(f"Can't move out of the table: (x->{self.x},y->{self.y},facing->{self.f})")
            else:
                table.maze[self.x][self.y] = 0
                self.x = self.x + 1
                table.maze[self.x][self.y] = 'R'
        elif self.f == 'w':
            if self.y == 0:
                raise Exception(f"Can't move out of the table: (x->{self.x},y->{self.y},facing->{self.f})")
            else:
                table.maze[self.x][self.y] = 0
                self.y = self.y - 1
                table.maze[self.x][self.y] = 'R'
        elif self.f == 'e':
            if self.x == len(table.maze)-1:
                raise Exception(f"Can't move out of the table: (x->{self.x},y->{self.y},facing->{self.f})")
            else:
                table.maze[self.x][self.y] = 0
                self.y = self.y + 1
                table.maze[self.x][self.y] = 'R'

    def Report(self,ixM):
        print(f"Robot is at x = {ixM[self.x]}, y = {self.y}, facing {self.f.upper()}")