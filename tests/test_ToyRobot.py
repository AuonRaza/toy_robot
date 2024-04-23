import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from ToyRobot import Table, Position

@pytest.fixture
def setup_table():
    table = Table(5, 5)  # Assuming 5x5 table for testing
    return table

def test_place_robot(setup_table):
    table = setup_table
    robot = Position()
    robot.Place(table, 2, 3, 'n')
    assert table.maze[2][3] == 'R'

def test_move_robot(setup_table):
    table = setup_table
    robot = Position()
    robot.Place(table, 2, 2, 'e')
    robot.Move(table)
    assert table.maze[2][2] == 0  # Previous position should be empty
    assert table.maze[2][3] == 'R'  # New position should have the robot

