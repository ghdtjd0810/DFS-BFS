# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:08:40 2022

@author: LG
"""

'''

def recursive_function(i):
    if i == 100:
        return
    print(i)
    recursive_function(i+1)
    print(i, '종료')
    
    
recursive_function(1)


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *=i
        
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    print(n)
    return n * factorial_recursive(n-1) # 여기서 n자체가 5,4,3,2로 줄



print(factorial_iterative(5),factorial_recursive(5))
'''
# In[1] DFS/BFS
'''
INF = int(1e9)

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)

graph= [[]for i in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))


graph[1].append((0,7))
graph[2].append((0,5))


print(graph)
'''

#결국 DFS의 개념은 노드를 방문했다는것을 스택으로 표현한다. 연결된간선은 인접리스트로 구현한다.
#방문한 stack은 True처리를 한다.


# 아 오키 이제 알겠다.
# if True이면 조건문이 실행되는 것 하나,
# if not False이면 조건문이 실행되는것 하나.
# 즉, False일때 조건문이 실행 될꺼라는 if not의 조건에 따라 DFS는 재귀함수를 돌리기 시작한다. 
def DFS(graph, v, visited):
    visited[v] = True # 재귀함수 종료 조건 
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i , visited)
            
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

visited = [False] * 9

DFS(graph, 1,visited)

