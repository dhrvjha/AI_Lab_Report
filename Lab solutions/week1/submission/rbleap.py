from collections import deque

def successor(state):
    possible_moves = []
    for ind in range(7):
        if state[ind] == 1:
            if ind + 1 < 7 and state[ind + 1] == 0:
                new_state = list(state)
                new_state[ind] = 0
                new_state[ind + 1] = 1
                possible_moves.append(tuple(new_state))
            if ind + 2 < 7 and state[ind + 2] == 0:
                new_state = list(state)
                new_state[ind] = 0
                new_state[ind + 2] = 1
                possible_moves.append(tuple(new_state))
        elif state[ind] == -1:
            if ind - 1 >= 0 and state[ind - 1] == 0:
                new_state = list(state)
                new_state[ind] = 0
                new_state[ind - 1] = -1
                possible_moves.append(tuple(new_state))
            if ind - 2 >= 0 and state[ind - 2] == 0:
                new_state = list(state)
                new_state[ind] = 0
                new_state[ind - 2] = -1
                possible_moves.append(tuple(new_state))
    return possible_moves

def dfs(initial_state, target_state):
    to_explore = [(initial_state, [])]
    explored = set()
    
    while to_explore:
        state, current_path = to_explore.pop()
        
        if state in explored:
            continue
        
        explored.add(state)
        updated_path = current_path + [state]
        
        if state == target_state:
            print("Total nodes explored:", len(explored))
            return updated_path
        
        for next_state in successor(state):
            to_explore.append((next_state, updated_path))
    
    return None

def bfs(initial_state, target_state):
    to_explore = deque([(initial_state, [])])
    explored = set()
    
    while to_explore:
        state, current_path = to_explore.popleft()
        
        if state in explored:
            continue
        
        explored.add(state)
        updated_path = current_path + [state]
        
        if state == target_state:
            print("Total nodes explored:", len(explored))
            return updated_path
        
        for next_state in successor(state):
            to_explore.append((next_state, updated_path))
    
    return None

start_state = (1, 1, 1, 0, -1, -1, -1)
goal_state = (-1, -1, -1, 0, 1, 1, 1)

print("Depth-First Search (DFS) Solution:")
dfs_result = dfs(start_state, goal_state)
if dfs_result:
    print("Solution found!")
    print("Steps count:", len(dfs_result) - 1)
    for step in dfs_result:
        print(step)
else:
    print("No solution exists.")

print("\nBreadth-First Search (BFS) Solution:")
bfs_result = bfs(start_state, goal_state)
if bfs_result:
    print("Solution found!")
    print("Steps count:", len(bfs_result) - 1)
    for step in bfs_result:
        print(step)
else:
    print("No solution exists.")