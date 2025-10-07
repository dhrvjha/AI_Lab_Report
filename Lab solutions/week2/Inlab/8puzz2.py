import heapq

class node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(s,gs):
    distance = 0
    for i in range(1,9):
        xi,yi=divmod(s.index(i),3)
        xj,yj=divmod(gs.index(i),3)
        distance += abs(xi-xj)+abs(yi-yj)
    return distance

def get_successors(n, goalstate):
    successors = []
    index = n.state.index(0)
    moves = [-1, 1, 3, -3]
    for move in moves:
        im = index + move
        if im >= 0 and im < 9:
            newstate = list(n.state)
            newstate[index],newstate[im]=newstate[im],newstate[index]
            g=n.g+1
            h=manhattan_distance(newstate, goalstate)
            successor=node(newstate,n,g,h)
            successors.append(successor)
    return successors

def astar(startstate,goalstate):
    start = node(startstate,None,0,manhattan_distance(startstate,goalstate))
    goal = node(goalstate)
    openlist = []
    heapq.heappush(openlist, start)
    visited = set()
    ne=0
    while openlist:
        n = heapq.heappop(openlist)      
        if tuple(n.state) in visited:
            continue
        visited.add(tuple(n.state))  
        ne+=1
        if n.state==goal.state:
            path=[]
            while n:
                path.append(n.state)
                n = n.parent
            print('Total nodes explored:',ne)
            return path[::-1]
        for s in get_successors(n, goalstate):
            if tuple(s.state) not in visited:
                heapq.heappush(openlist, s)

    print('Total nodes explored:',ne)
    return None

startstate=[1, 2, 3, 4, 5, 6, 7, 8, 0]
goalstate=[1, 2, 3, 4, 5, 6, 0, 7, 8]

solution=astar(startstate,goalstate)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
