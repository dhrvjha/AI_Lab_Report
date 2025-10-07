import string as strg
import random as rnd
from itertools import combinations
import numpy as np

def ask(m):
    return int(input(m))

def mkfmls(fc, vf, tv):
    lv = list(strg.ascii_lowercase[:tv])
    uv = [v.upper() for v in lv]
    symbs = lv + uv
    mx, unq = 20, set()
    combs = list(combinations(symbs, vf))
    i = 0
    while len(unq) < fc and i < mx:
        nf = tuple(sorted(rnd.choice(combs)))
        if nf not in unq:
            unq.add(nf)
        i += 1
    return [list(f) for f in unq]

def mkasn(symbs, tv):
    la = list(np.random.choice(2, tv))
    ua = [1 - i for i in la]
    return dict(zip(symbs, la + ua))

def evlfml(fml, asn):
    return sum(any(asn[v] for v in c) for c in fml)

def hclimb(fml, asn, ps, fs, ts):
    ba = asn.copy()
    ms, ma = ps, asn.copy()
    for k, v in asn.items():
        ts += 1
        ta = asn.copy()
        ta[k] = 1 - v
        s = evlfml(fml, ta)
        if s > ms:
            fs, ms, ma = ts, s, ta.copy()
    if ms == ps:
        return ba, ms, f"{fs}/{ts - len(asn)}"
    return hclimb(fml, ma, ms, fs, ts)

def bsrch(fml, asn, bw, sc):
    if evlfml(fml, asn) == len(fml):
        return asn, f"{sc}/{sc}"
    cands = []
    for k, v in asn.items():
        sc += 1
        na = asn.copy()
        na[k] = 1 - v
        s = evlfml(fml, na)
        cands.append((na, s, sc))
    best = sorted(cands, key=lambda x: x[1])[-bw:]
    if len(fml) in [c[1] for c in best]:
        sol = next(c for c in best if c[1] == len(fml))
        return sol[0], f"{sol[2]}/{sc}"
    return bsrch(fml, best[-1][0], bw, sc)

def vnbhd(fml, asn, ns, step):
    if evlfml(fml, asn) == len(fml):
        return asn, f"{step}/{step}", ns
    cands = []
    for k, v in asn.items():
        step += 1
        na = asn.copy()
        na[k] = 1 - v
        s = evlfml(fml, na)
        cands.append((na, s, step))
    best = sorted(cands, key=lambda x: x[1])[-ns:]
    if len(fml) in [c[1] for c in best]:
        sol = next(c for c in best if c[1] == len(fml))
        return sol[0], f"{sol[2]}/{step}", ns
    return vnbhd(fml, best[-1][0], ns + 1, step)

def run():
 
    fc = int(input("Formula: "))
    vf = int(input("Variable per formula: "))
    tv = int(input("Total var: "))
    fmls = mkfmls(fc, vf, tv)
    symbs = list(strg.ascii_lowercase[:tv]) + [c.upper() for c in strg.ascii_lowercase[:tv]]
   
    for i, fml in enumerate(fmls, 1):
        print(f"\n {i}: {fml}")
        ia = mkasn(symbs, tv)
        is_ = evlfml(fml, ia)
        _, hs, hp = hclimb(fml, ia, is_, 1, 1)
        ba, bp = bsrch(fml, ia, 3, 1)
        va, vp, vn = vnbhd(fml, ia, 1, 1)
        print(f"HC: S={hs}, P={hp}")
        print(f"BS: S={evlfml(fml, ba)}, P={bp}")
        print(f"VND: S={evlfml(fml, va)}, P={vp}, N={vn}")

if __name__ == "__main__":
    run()