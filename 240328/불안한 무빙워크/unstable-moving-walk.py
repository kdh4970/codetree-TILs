# 무빙워크 판의 개수 N, 안정성이 0인 판의 개수가 K일 떄 실험 종료
# 종료 조건 : 안정성이 0인 판이 K개
# 
from collections import deque

N, K = list(map(int,input().split()))
moving_walk = deque(list(map(int,input().split())))


def simul():
    cnt = 0
    person = deque()
    while True:
        #1
        cnt += 1
        moving_walk.rotate(1)
        if person:
            for _ in range(len(person)):
                person[_] += 1
            if N-1 in person:
                person.popleft()
        #2
        if person:
            for _ in range(len(person)):
                if person[_]+1 in person or moving_walk[person[_]+1] == 0:
                    continue
                person[_] += 1
                moving_walk[person[_]] -= 1
            
            if N-1 in person:
                person.popleft()
        #3
        if 0 not in person and moving_walk[0] > 0:
            person.append(0)
            moving_walk[0] -=1
            if N-1 in person:
                    person.popleft()
        #4
        if moving_walk.count(0) >= K:
            return cnt
        

print(simul())