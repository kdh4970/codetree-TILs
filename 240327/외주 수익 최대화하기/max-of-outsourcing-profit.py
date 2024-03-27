# n 일간 외주 개발
# 1일부터 day에 t[i]를 더하고, money에 p[i]를 더해가며
# day가 n+1 이면 종료

N = int(input())
t = []
p = []
for _ in range(N):
    temp_t,temp_p = list(map(int,input().split()))
    t.append(temp_t)
    p.append(temp_p)
lst = []
last_pay = 0

def func(day,money):
    global last_pay
    if day == N+1:
        lst.append(money)
        return
    elif day > N+1:
        lst.append(money-last_pay)
        return
    else:
        last_pay = p[day-1]
        func(day+t[day-1],money+p[day-1])
        func(day+1,money)



func(1,0)
print(max(lst))