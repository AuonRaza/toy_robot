from Table import Table
from Position import Position
from IndexMapping import IndexMapping

x = int(input("Enter the size of dimesion X: "))
y = int(input("Enter the size of dimesion Y: "))

table = Table(x,y)

robot = Position()
esc = False

def GetXY(p):
    nums = p.replace("(","").replace(",","").replace(")","")
    p = []
    for num in nums:
        if num.isnumeric():
            p.append(int(num))
    return p

while (esc != True):
    print("What is your next Move?")
    print("1. Place(x,y,f)\n2. Left\n3. Right\n4. Report\n5. Move\nOR INPUT EXIT TO QUIT!")
    choice = input("Enter a choice: ")
    if choice.lower()!="exit":
        if int(choice) == 1:
            pos = input("Enter Position (X,Y): ")
            posX, posY = GetXY(pos)

            facing = input("Enter facing: ")
            robot.Place(table, posY, posX, facing)
        elif int(choice) == 2:
            robot.TurnLeft()
        elif int(choice) == 3:
            robot.TurnRight()
        elif int(choice) == 4:
            robot.Report()
        elif int(choice) == 5:
            robot.Move(table)
    else:
        esc = True
