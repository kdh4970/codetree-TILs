from collections import deque
N = int(input())

# student = [list(map(int,input().split())) for _ in range(N**2)]
student=[]
stdtoidx = {}
for _ in range(N**2):
    line = list(map(int,input().split()))
    stdtoidx[line[0]] = _ 
    student.append(line)


seat = [[0]*N for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def search_seat(start_point,std,cnt):
    isVisit = [[0]*N for _ in range(N)]
    q = deque()
    q.append(start_point)
    possible_seat = {}
    while q:
        now_r,now_c = q.popleft()
        n_like = 0
        empty = 0
        isVisit[now_r][now_c] = 1
        for _ in range(4):
            search_r,search_c = now_r+dx[_],now_c+dy[_]
            if not 0 <= search_r <= N-1 or not 0 <= search_c <= N-1:
                continue
            if seat[search_r][search_c] in std[1:]:
                n_like += 1
            elif seat[search_r][search_c] == 0: 
                if cnt == N**2-1:
                    seat[search_r][search_c] = std[0]
                    return
                empty += 1
            if isVisit[search_r][search_c]==0:
                q.append((search_r,search_c))
                isVisit[search_r][search_c]=1
        if seat[now_r][now_c] > 0:continue
        possible_seat[(-now_r,-now_c)] = (n_like,empty)
    possible_seat = sorted(possible_seat.items(),key = lambda x:(x[1][0],x[1][1],x[0][0]),reverse = True)
    # print(possible_seat)
    
    for _ in range(len(possible_seat)):
        now_pos, now_val = possible_seat[_]
        if _ == len(possible_seat)-1:
            seat[-now_pos[0]][-now_pos[1]] = std[0]
            break
        
        next_pos,next_val = possible_seat[_+1]
        if now_val[0] > next_val[0]:
            seat[-now_pos[0]][-now_pos[1]] = std[0]
            break
        if now_val[1] > next_val[1]:
            seat[-now_pos[0]][-now_pos[1]] = std[0]
            break
        if -now_pos[0] < -next_pos[0]:
            seat[-now_pos[0]][-now_pos[1]] = std[0]
            break
        elif -now_pos[0] > -next_pos[0]:
            continue
        if -now_pos[1] < -next_pos[1]:
            seat[-now_pos[0]][-now_pos[1]] = std[0]
            break
        
for _ in range(N**2):
    search_seat((0,0),student[_],_)

# print(seat)
score = 0
for row in range(N):
    for col in range(N):
        cnt = 0
        for _ in range(4):
            search_r,search_c = row+dx[_], col+dy[_]
            if not 0 <= search_r <=N-1 or not 0<= search_c <= N-1:
                continue
            target = stdtoidx[seat[row][col]]

            if seat[search_r][search_c] in student[target][1:]:
                cnt+=1
        score += 10**(cnt-1) if cnt > 0 else 0

print(score)