nums = input()

numbers = nums.split()

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

# print(min(a, b, c), max(a, b, c))

min = a
max = a

if b < min:
    min = b
if c < min:
    min = c 
if b > max:
    max = b
if c > max:
    max = c

print(min, max)