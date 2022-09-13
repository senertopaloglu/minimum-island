def minimum_island(grid):
  visited = set()
  minsize = float("inf")
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if (i, j) in visited:
        continue
        
      if grid[i][j] == "W":
        continue
      
      minsize = min(minsize, discover(grid, i, j, visited))

  return minsize

def discover(grid, row, col, visited):
  rowbound = 0 <= row < len(grid)
  colbound = 0 <= col < len(grid[0])
  
  if not rowbound or not colbound:
    return 0
  
  if grid[row][col] == "W":
    return 0
  
  if (row,col) in visited:
    return 0
  
  visited.add((row,col))
  
  return 1 + discover(grid, row-1, col, visited) + discover(grid, row + 1, col, visited) + discover(grid, row, col-1, visited) + discover(grid, row, col+1, visited)
