import heapq
import re

class node:
    def __init__(self, state, parent=None,g=0,h=0):
        self.state=state
        self.parent=parent
        self.g=g
        self.h=h
        self.f=g+h
    def __lt__(self,other):
        return self.f<other.f

def gns(n,doc1,doc2):
    ns=[]
    idx1,idx2 = n.state
    if idx1 < len(doc1) and idx2 < len(doc2):
        newstate = (idx1 + 1, idx2 + 1)
        ns.append(node(newstate, n))
    if idx1 < len(doc1):
        newstate = (idx1 + 1, idx2)
        ns.append(node(newstate, n))
    if idx2 < len(doc2):
        newstate = (idx1, idx2 + 1)
        ns.append(node(newstate, n))
    return ns

def ct(text):
    return re.sub(r'[^\w\s]','',text.lower())

def estimate(state,doc1,doc2):
    i1,i2=state
    return ((len(doc1)-i1)+(len(doc2)-i2))

def levenshtein(s1, s2):
    m,n=len(s1),len(s2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=0
            elif j==0:
                dp[i][j]=0
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]


def astar(doc1,doc2):
    ss = (0, 0)
    gs = (len(doc1), len(doc2))
    start = node(ss)
    openlist = []
    heapq.heappush(openlist, (start.f, start))
    explored = set()
    while openlist:
        _, n = heapq.heappop(openlist)
        if n.state in explored:
            continue
        explored.add(n.state)
        if n.state == gs:
            path = []
            while n:
                path.append(n.state)
                n = n.parent
            return path[::-1]
        for s in gns(n, doc1, doc2):
            idx1, idx2 = s.state
            if idx1 < len(doc1) and idx2 < len(doc2):
                s.g = n.g + levenshtein(doc1[idx1], doc2[idx2])
            else:
                s.g = n.g + 1
            s.h=estimate(s.state, doc1, doc2)
            s.f = s.g + s.h
            heapq.heappush(openlist, (s.f, s))

    return None

def check_plagiarism(doc1,doc2):
    doc1 = [ct(sent) for sent in doc1]
    doc2 = [ct(sent) for sent in doc2]

    alignment=astar(doc1, doc2)
    similar_pairs = []
    for i, j in alignment:
        if i < len(doc1) and j < len(doc2):
            s1,s2 = doc1[i], doc2[j]
            maxi = max(len(s1),len(s2))
            if maxi> 0:
                simi=1-(levenshtein(s1,s2)/maxi)
                if simi>=0.5:
                    similar_pairs.append((doc1[i],doc2[j],simi))
    return similar_pairs

doc1=[
    "This is a sample document.",
    "Another one comes here.",
]

doc2=[
    "This is a sample doc.",
    "This one might be copied.",  
]

plagiarism = check_plagiarism(doc1, doc2)
if plagiarism:
    print("Potential plagiarism detected:")
    for pair in plagiarism:
        print(f"Doc1: {pair[0]} \nDoc2: {pair[1]} \nSimilar percentage {pair[2]*100}%")
else:
    print("No plagiarism detected.")
