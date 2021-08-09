from collections import deque

S1=["A","B","C"]
S2=deque(S1)
print(S2)
S2.popleft()
print(S2)
S2.popleft()
print(S2)
S2.popleft()
print(S2)
if not S2:
    print("No Element Left")