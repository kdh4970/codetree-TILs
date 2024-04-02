# N = 0, S = 1
from collections import deque

seat = []
isrotate = None
for _ in range(4):
    line = input()
    seat.append(deque([int(_) for _ in line]))

K = int(input())

target_rotate_list = []
direction_list = []
for _ in range(K):
    r,d = list(map(int,input().split()))
    target_rotate_list.append(r-1)
    direction_list.append(d)

def RotateSeat(target,direction,connect):
    global isrotate
    seat[target].rotate(direction)
    isrotate[target] = True
    if target < 0 or target > 3:
        return
    
    if target-1 >= 0 and connect[target-1] and isrotate[target-1] == False:
        RotateSeat(target-1,-direction,connect)
    if target +1 <= 3 and connect[target] and isrotate[target+1] == False:
        RotateSeat(target+1,-direction,connect)

for target,direction in zip(target_rotate_list,direction_list):
    connect = [not seat[_][2] == seat[_+1][-2] for _ in range(3)]
    isrotate = [False] * 4
    RotateSeat(target,direction,connect)




res = 0
for idx,_ in enumerate(seat):
    if _[0] == 0: continue
    res += 2**idx
print(res)