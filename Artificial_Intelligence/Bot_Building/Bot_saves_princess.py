#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    center = n - ((n-1)/2) - 1
    
    
    princess = 'p'
    
    for i in range(n):
        if princess in grid[i]:
            a = grid[i].index('p')
            b = i
            break
            
    x = a-center
    y = b-center
    
    d = int((n-1)/2)
    
    for i in range(d):
        if x > 0:
            print('RIGHT')
        else:
            print('LEFT')
            
    for i in range(d):
        if y > 0:
            print('DOWN')
        else:
            print('UP')    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
