n = int(input())

numbers = list(map(int, input().split()))

l = min(numbers)
i = numbers.index(l)

print(l, i+1)