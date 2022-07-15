

#### Important Please Read this #####
# #### Please install Pathfinding package for python using pip install pathfinding command in linux as it is vital for this program to function properly  

from pathfinding.core.grid import Grid                           
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
  [1, 1, 0, 0, 1, 0, 1, 0, 1, 1],
  [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
  [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
  [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 1. create the grid with the nodes 
grid = Grid(matrix=matrix)

# get start and end point 
start = grid.node(0, 0)
end = grid.node(9, 9)

# create a finder with the movement style    # using A* star algorithm to determine the path on 2D matrix
finder = AStarFinder(diagonal_movement = DiagonalMovement.always) 



# returns a list with the path and the amount of times the finder had to run to get the path 
path, runs = finder.find_path(start, end, grid)

#Prints the location of additionallly placed location
print("Random Placed Obstacles: [(2, 0), (3, 0), (5, 0), (7, 0), (4, 1), (8, 1), (1, 2), (9, 2), (3, 3), (5, 3), (7, 3), (0, 4), (3, 4), (8, 4), (3, 5), (5, 5), (0, 6), (4, 7), (0, 8), (0, 9)]")

#Path If statement for bonus phase
if path == []: #checks if the print path is empty
  print("Unable to Reach delivery point")
else:
  print("Robot's path:", path ) #prints the path

