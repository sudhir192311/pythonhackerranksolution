from itertools import groupby

n = input().strip()

for key, group in groupby(n):
    print((len(list(group)), int(key)), end=" ")