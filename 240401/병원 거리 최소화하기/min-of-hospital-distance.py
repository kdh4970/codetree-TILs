# 병원을 M개로 줄일 때, 각 사람들의 병원 까지의 거리의 총합의 최솟값
# 전체 병원 중 M개 샘플링, 각 케이스마다 거리의 총합을 계산.
# 계산 도중 최솟값을 넘어서는 케이스는 중단 후 다음 케이스로
# 각 사람에 대해 병원 까지 최소거리를 구하는 함수 - BFS
# 전체 병원에서 N개 샘플링
# 전체에서 총합 최솟값 - 재귀 백트래킹
# 종료조건 : 

from collections import deque

N,M = list(map(int,input().split()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# city = [list(map(int,input().split())) for _ in range(N)]
city = []
hosp = []
person = []

for row in range(N):
    line = list(map(int,input().split()))
    city.append(line)
    for col in range(N):
        if line[col] == 2:
            hosp.append((row,col))
        elif line[col] == 1:
            person.append((row,col))


def getMindistPerPerson(_person_pos,_hospital):
    q = deque()
    q.append(_person_pos)
    minDist = 2*N
    dstMap = [[-1]*N for _ in range(N)]
    dst = 0
    while q:
        now_r,now_c = q.popleft()
        if dst == 0:
            dstMap[now_r][now_c] = dst
            dst += 1
        else:
            dst = dstMap[now_r][now_c] +1
        for _ in range(4):
            search_r, search_c = now_r+dx[_], now_c+dy[_]
            if not 0 <= search_r < N or not 0 <= search_c < N or dstMap[search_r][search_c] > -1 :
                continue
            if (search_r,search_c) in _hospital:
                minDist = dst if dst < minDist else minDist
                # print(dstMap)
                # print(minDist)
                return minDist
            dstMap[search_r][search_c] = dst
            q.append((search_r,search_c))

sampledHosp = []

minsum = 1e6

def sampleM(cnt,lst):
    global minsum
    if len(lst) == M:
        # sampledHosp.append(lst.copy())
        temp = 0
        for p in person:
            if temp > minsum: return
            temp += getMindistPerPerson(p,lst)
        minsum = temp if temp < minsum else minsum
        return
    for _ in range(len(hosp)):
        if _ < cnt or hosp[_] in lst:
            continue
        lst.append(hosp[_])
        sampleM(_,lst)
        lst.pop()

sampleM(0,[])
# print(hosp)
# print(sampledHosp)


# def getMindistTotal(_hosp):
#     return sum(getMindistPerPerson(p,_hosp) for p in person)
# print(min(getMindistTotal(_) for _ in sampledHosp))

print(minsum)