import time
import heapq

class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.action = None
        self.g = g  

    def __lt__(self, other):
        return self.g < other.g  

goal_state = [
    [2, 2, 0, 0, 0, 2, 2],
    [2, 2, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [2, 2, 0, 0, 0, 2, 2],
    [2, 2, 0, 0, 0, 2, 2]
]
initial_state = [
    [2, 2, 1, 1, 1, 2, 2], 
    [2, 2, 1, 1, 1, 2, 2], 
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 1], 
    [2, 2, 1, 1, 1, 2, 2],
    [2, 2, 1, 1, 1, 2, 2]
]

v = 0

def succesor(node):
    global v
    successors = []
    dm = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    mm = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(7):
        for y in range(7):
            if node.state[x][y] == 1:
                for d in range(4):
                    nx, ny = x + dm[d][0], y + dm[d][1]
                    midx, midy = x + mm[d][0], y + mm[d][1]

                    if 0 <= nx < 7 and 0 <= ny < 7 and node.state[midx][midy] == 1 and node.state[nx][ny] == 0:
                        ns = [row[:] for row in node.state]
                        ns[x][y] = 0
                        ns[midx][midy] = 0
                        ns[nx][ny] = 1
                        child_node = Node(ns, node, g=node.g + 1)
                        child_node.action = [(x, y), (nx, ny)]
                        successors.append(child_node)
                        v += 1
    return successors

def pqs():
    frontier = []
    explored = set()

    start_node = Node(initial_state)
    heapq.heappush(frontier, start_node)

    while frontier:
        current_node = heapq.heappop(frontier)

        print("Current state with path cost:", current_node.g)
        for row in current_node.state:
            print(row)
        print()

        if (current_node.state == goal_state):
            print("Search completed")
            return current_node

        explored.add(str(current_node.state))

        for child in succesor(current_node):
            if str(child.state) not in explored:
                heapq.heappush(frontier, child)

    return None

def eact(goal_node):
    actions = []
    while goal_node.parent:
        actions.append(goal_node.action)
        goal_node = goal_node.parent
    return actions[::-1]

print("Priority Queue Search started")
start_time = time.time()
result_node = pqs()
end_time = time.time()

if result_node:
    print("Total nodes expanded:", v)
    print("time:", end_time - start_time)
    print("Final state:")
    for row in result_node.state:
        print(row)
    print("\nMoves:")
    moves = eact(result_node)
    for move in moves:
        print(move)
else:
    print("No solution found.")
