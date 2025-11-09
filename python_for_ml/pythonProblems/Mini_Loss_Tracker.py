n = int(input())
t = float(input())
sum = 0.00
for i in range(n):
    l = float(input())
    sum += l

avg = sum / n

if avg <= t:
    print("PASS")
else:
    print("RETRY")
