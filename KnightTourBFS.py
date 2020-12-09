#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:06:42 2020

@author: jharnadohotia
"""

# Python3 code to find minimum steps to reach 
# to specific cell in minimum moves by Knight 

N = 8
chess = [[(j)+N*i for j in range(0,N)] for i in range(0,N)]

def index_2d(chess, v):
    for i, x in enumerate(chess):
        if v in x:
            return ([i, x.index(v)])
    
def valid(x,y,N):
        if (x >= 1 and x <= N and y >= 1 and y <= N):  
            return True
        return False   

def pos(src,des):
    x,y = index_2d(chess, src) , index_2d(chess, des)
    return ([x,y])

def KnightTour(knightpos, targetpos, N): 
      
    # all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
      
    queue = [] 
      
    # push starting position of knight 
    # with 0 distance 
    queue.append([knightpos[0], knightpos[1], 0]) 
      
    # make all cell unvisited  
    visited = [[False for i in range(N + 1)]  
                      for j in range(N + 1)] 
      
    # visit starting state 
    visited[knightpos[0]][knightpos[1]] = True
      
    # loop untill we have one element in queue  
    while(len(queue) > 0): 
          
        t = queue[0] 
        queue.pop(0) 
          
        # if current cell is equal to target  
        # cell, return its distance  
        if(t[0] == targetpos[0] and 
           t[1] == targetpos[1]): 
            return t[2] 
              
        # iterate for all reachable states  
        for i in range(8): 
              
            x = t[0] + dx[i] 
            y = t[1] + dy[i] 
              
            if(valid(x, y, N) and not visited[x][y]): 
                visited[x][y] = True
                queue.append([x, y, t[2] + 1]) 

s,d = pos(0,1)
print (s)
print (d)

print(KnightTour(s, d, N))

