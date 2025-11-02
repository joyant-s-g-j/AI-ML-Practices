n = int(input())
a = list(map(int, input().split()))

mn = lambda x: min(x)
mx = lambda x: max(x)

print(mn(a), mx(a))