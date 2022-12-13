# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

(K, N) = map(int, input().split())

L = list()
for i in range(K):
    l = map(int, input().split())
    m=list(l)
    n = m[0]
    L.append(m[1:])
    assert len(L[i]) == n

S_max = 0
L_max = None

for l in itertools.product(*L):
    s = sum([x**2 for x in l]) % N

    if s > S_max:
        S_max = s
        L_max = l

print(S_max)




# n=3
# m=1000
# ll=[[2,5,4],[3,7,8,9],[5,5,7,8,9,10]]
# sum=0
# for l in ll:
#     temp=max(l)
#     print(temp)
#     if(sum==0):
#         sum+=sum+(temp**2)
#     else:
#         sum+=(temp**2)
        
# print(sum)
    
