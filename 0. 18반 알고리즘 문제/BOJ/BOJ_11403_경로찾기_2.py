import sys
sys.stdin = open('input.txt', 'r')

import itertools as p
i,u,r,m,l,p,t = int,input,range,map,list,p.product,print
n=r(i(u()));g=[l(m(i, u().split()))for _ in n]
for m,s,t in p(n,repeat=3):g[s][t]=g[s][t]|(g[s][m]&g[m][t])
for l in g:t(*l)