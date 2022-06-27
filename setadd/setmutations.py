
length = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    (operation_name, other_set_length) = input().split()
    other_set = set(map(int,input().split()))

    if operation_name == 'intersection_update':
        A.intersection_update(other_set)
    elif operation_name == 'update':
        A.update(other_set)
    elif operation_name == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif operation_name == 'difference_update':
        A.difference_update(other_set)
    else:
        assert False

print(sum(A))