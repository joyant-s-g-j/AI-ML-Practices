n = int(input())

numbers = list(map(int, input().split()))

min = min(numbers)
max = max(numbers)

min_i = numbers.index(min)
max_i = numbers.index(max)

numbers[min_i], numbers[max_i] = numbers[max_i], numbers[min_i]

print(*numbers)