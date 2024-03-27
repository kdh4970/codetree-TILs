N = int(input())
numbers = list(map(int,input().split()))
operators = list(map(int,input().split()))


res_min = numbers[0]
res_max = numbers[0]

operator_lst=[]
lst = []

def gen_oper_list(num_operator):
    if num_operator == 0:
        operator_lst.append(lst.copy())
        return
    for _ in range(3):
        if operators[_]:
            lst.append(_)
            operators[_] -= 1
            gen_oper_list(num_operator-1)
            lst.pop()
            operators[_] =+ 1


gen_oper_list(sum(operators))

for opers in operator_lst:
    temp = numbers[0]
    for _ in range(N-1):
        if opers[_] == 0:
            temp += numbers[_+1]
        elif opers[_] == 1:
            temp -= numbers[_+1]
        elif opers[_] == 2:
            temp *= numbers[_+1]
    if temp > res_max:
        res_max = temp
    if temp < res_min:
        res_min = temp
    if len(operator_lst) == 1:
        res_min = temp
        res_max = temp

print(res_min,res_max)