# 병원을 M개로 줄일 때, 각 사람들의 병원 까지의 거리의 총합의 최솟값
# 전체 병원 중 M개 샘플링, 각 케이스마다 거리의 총합을 계산.
# 계산 도중 최솟값을 넘어서는 케이스는 중단 후 다음 케이스로
# 각 사람에 대해 병원 까지 최소거리를 구하는 함수 - 문제에 주어짐
# 전체 병원에서 N개 샘플링
# 전체에서 총합 최솟값 - 재귀 백트래킹


from collections import deque

N,M = list(map(int,input().split()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

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
    px,py = _person_pos
    mindst = 2*N
    for h in _hospital:
        dst = abs(px-h[0]) + abs(py-h[1])
        mindst = dst if dst < mindst else mindst
    return mindst


sampledHosp = []

minsum = 1e6

def sampleM(cnt,lst):
    global minsum
    if len(lst) == M:
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

print(minsum)