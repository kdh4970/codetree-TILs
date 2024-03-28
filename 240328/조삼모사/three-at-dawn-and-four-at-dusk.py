# n개의 일이 주어질 때, 아침 저녁으로 n/2개 씩 처리
# 나누어서 하는 일이 2,3,4,5일때
# 더해야 할 강도 수 1*2,3*2,6*2, 10*2
#                1,1+2,1+2+3,1+2+3+4 의 두배
# k개 일에 대해 강도 총합은 sum(1 ~ k-1) * 2
# 아침 강도와 저녁 강도의 차의 최솟값

# n 개의 일을 n/2개로 분할 시 나오는 경우의 수 k, k[0] k[-1]은 아침 저녁 일 관계, 즉 코스트도 k개에 대해서 구하고, 양끝에서부터 합계산
# 강도를 구하는 함수

N = int(input())
p = [list(map(int,input().split())) for _ in range(N)]

def getCost(job1,job2):
    return p[job1][job2] + p[job2][job1]

def getTotalCost(job_list):
    total = 0
    for job1 in job_list:
        for job2 in job_list:
            if job1 == job2 or job2 > job1:continue
            total += getCost(job1,job2)
    return total

job_list = []
cost_list = []
temp = []

def AllocJob(job_num):
    if len(temp) == N//2:
        job_list.append(temp.copy())
        cost_list.append(getTotalCost(tuple(temp)))
        return
    for _ in range(N):
        if _ < job_num or _ in temp:continue
        temp.append(_)
        AllocJob(_)
        temp.pop()


AllocJob(0)

min_cost_diff = 2**32-1
for _ in range(len(cost_list)//2):
    day_cost = cost_list[_]
    night_cost = cost_list[len(cost_list)-1-_]
    cost_diff = abs(day_cost-night_cost)
    min_cost_diff = cost_diff if min_cost_diff > cost_diff else min_cost_diff

# print(job_list)
# print(cost_list)
print(min_cost_diff)