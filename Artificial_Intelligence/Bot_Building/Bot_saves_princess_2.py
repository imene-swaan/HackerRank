def nextMove(n,r,c,grid):
    
    princess = 'p'
    
    for i in range(n):
        if princess in grid[i]:
            x = grid[i].index('p')
            y = i
            break
            
  
    
    a = x-c
    b = y-r
    
    
    if a != 0:
        if a > 0:
            r = 'RIGHT'
        else:
            r = 'LEFT'
     
    if b != 0:
        if b > 0:
            r = 'DOWN'
        else:
            r = 'UP'
            
    return r

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
