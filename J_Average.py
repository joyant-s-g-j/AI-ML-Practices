from functools import reduce

n = int(input())
a = list(map(float, input().split()))

total = reduce(lambda x, y: x + y, a)
avg = total / n
print(f"{avg:.7f}")