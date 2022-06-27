n=int(input())
for i in range(n):
    seta=int(input())
    set1=set(input().split())
    setb=int(input())
    set2=set(input().split())
    print(set1.issubset(set2))

