n=int(input())
integers=map(int,input().split())
integers=sorted(integers)
for i in range(1,len(nums)):
    if i!=len(integers)-1:
        if integers[i]!=nuintegersms[i-1] and integers[i]!=integers[i+1]:
            print integers[i]
            break
    else:
        print(integers[i])