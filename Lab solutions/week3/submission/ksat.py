import string
import random
from itertools import combinations

def getinput(prompt):
    return int(input(prompt))

def generaterandomclauses(cc, vc, tv):
    lvars=list(string.ascii_lowercase[:tv])
    uvars=[v.upper() for v in lvars]
    allvariables=lvars + uvars
    
    maxi = 18
    unik = set()
    allv = list(combinations(allvariables, vc))
    
    at = 0
    while len(unik) < cc and at < maxi:
        newclause = tuple(sorted(random.sample(allv,1)[0]))
        if newclause not in unik:
            unik.add(newclause)
        at += 1
    
    return [list(clause) for clause in unik]

def main():
    print("Random Clause Generator")
    cc = getinput("Enter the number of clauses: ")
    vc = getinput("Enter the number of variables in a clause: ")
    tv = getinput("Enter the total number of variables: ")
    for _,clause in enumerate(generaterandomclauses(cc,vc,tv), 1):
        print(f"{clause}")

if __name__ == "__main__":
    main()
