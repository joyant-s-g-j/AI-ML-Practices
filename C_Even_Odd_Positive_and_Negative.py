n = int(input())

nums = input()

numbers = nums.split()

even = 0
odd = 0
positive = 0
negative = 0

for i in range(n):
    a = int(numbers[i])
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    if a > 0:
        positive += 1
    elif a < 0:
        negative += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)