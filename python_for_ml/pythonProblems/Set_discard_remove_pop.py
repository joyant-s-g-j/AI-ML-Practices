n = int(input())
nums = list(map(int, input().split()))
s = set(nums)
ins = int(input())
for i in range(ins):
    cmd = input().split()
    if cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
    elif cmd[0] == "pop":
        s.pop()
print(sum(s))