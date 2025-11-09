n = list(map(int, input().split()))

avg = sum(n) / len(n)

if avg < 85:
    print("Dark Image")
elif avg <= 170:
    print("Normal Image")
else:
    print("Bright Image")
