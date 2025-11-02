s = list(map(str, input().split()))
k = ["ai", "data", "model", "learn", "train", "neural"]
c = 0
for i in s:
    if i.lower() in k:
        c += 1
if c >= 2:
    print("AI Detected")
else:
    print("Not AI Related")