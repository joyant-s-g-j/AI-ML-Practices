n = int(input())

YES_count = 0
NO_count = 0

for i in range(n):
    l = input()

    if l == "YES":
        YES_count += 1
    else:
        NO_count += 1
        
if YES_count >= NO_count:
    print("ACCEPT")
else:
    print("REJECT")