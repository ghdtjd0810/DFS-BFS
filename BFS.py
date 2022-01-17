# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 12:51:36 2022

@author: LG
"""

from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True
    
    
    # 조건문, queue라는 리스트가 있을때는 계속 돌아간다는 말이 되겠지. 
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        # v자체가 함수, poplieft임. 그러니까 grpah[v] 는 queue 에 있는쩰 처음 들어온 숫자를 하나 뺀 거를 확인해본다는 의미임. 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                print(queue, 'queue')
                visited[i] = True
            
            

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] *9
bfs(graph, 1, visited)
