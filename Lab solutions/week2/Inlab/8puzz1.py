from collections import deque

class node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def get_successors(n):
    successors = []
    index = n.state.index(0)
    moves = [-1, 1, 3, -3]
    for move in moves:
        i = index + move
        if i >= 0 and i < 9:
            ns = list(n.state)
            temp = ns[i]
            ns[i] = ns[index]
            ns[index] = temp
            successor = node(ns, n)
            successors.append(successor)
    return successors

def bfs(startstate, goalstate):
    start = node(startstate)
    goal = node(goalstate)
    q = deque([start])
    visited = set()
    nodesexplored = 0
    while q:
        n = q.popleft()
        if tuple(n.state) in visited:
            continue
        visited.add(tuple(n.state))
        print(n.state)
        nodesexplored += 1
        if n.state == list(goal.state):
            path = []
            while n:
                path.append(n.state)
                n = n.parent
            print('Total nodes explored', nodesexplored)
            return path[::-1]
        for s in get_successors(n):
            q.append(s)
    print('Total nodes explored', nodesexplored)
    return None

startstate=[1, 2, 3, 4, 5, 6, 7, 8, 0]
goalstate=[1, 2, 3, 4, 5, 6, 0, 7, 8]

solution = bfs(startstate,goalstate)

if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
