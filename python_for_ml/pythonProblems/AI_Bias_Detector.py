n = input().split()
ac = 0
bc = 0
nc = len(n)

for i in range(nc):
    if n[i] == 'A':
        ac += 1
    else:
        bc += 1

pa = (ac / nc) * 100
pb = (bc / nc) * 100

if pa > 70 or pb > 70:
    print("Biased Model")
else:
    print("Fair Model")