N = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))

oper_list = []
temp = []

def makeOperList(n):
    if n == N-1:
        oper_list.append(temp.copy())
        return
    
    for op in range(len(operators)):
        if operators[op]:
            temp.append(op)
            operators[op] -= 1
            makeOperList(n+1)
            operators[op] += 1
            temp.pop()

makeOperList(0)

res_max = 0
res_min = 0

for case, test in enumerate(oper_list):
    x = numbers[0]
    for idx in range(N-1):
        if test[idx] == 0:
            x += numbers[idx+1]
        elif test[idx] == 1:
            x -= numbers[idx+1]
        elif test[idx] == 2:
            x *= numbers[idx+1]
    if case == 0:
        res_min = x
        res_max = x
    if res_max < x : res_max = x
    if res_min > x : res_min = x

print(res_min,res_max)