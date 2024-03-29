from collections import deque

N,L,R = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
stop = False
moved = False

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(row,col):
    global stop, moved
    q = deque()
    q.append((row,col))
    union = []
    while q:
        now = q.popleft()
        union.append(now)
        for _ in range(4):
            temp_r = now[0] + dr[_]
            temp_c = now[1] + dr[_]
            if temp_r < 0 or temp_r > N-1 or temp_c < 0 or temp_c > N-1 or visited[temp_r][temp_c]:
                continue
            if L <= abs(board[now[0]][now[1]] - board[temp_r][temp_c]) <= R:
                visited[temp_r][temp_c] = True
                q.append((temp_r,temp_c))
                union.append((temp_r,temp_c))
    if len(union) == 1:
        stop = True
    else:
        stop = False
        moved = True
        total = 0
        for r,c in union:
            total += board[r][c]
        new = total// len(union)
        for r,c in union:
            board[r][c] = new

cnt = 0
while not stop:
    moved = False
    for r in range(N):
        for c in range(N):
            if visited[r][c] == True:
                continue
            bfs(r,c)
    if moved : cnt+=1

print(cnt)