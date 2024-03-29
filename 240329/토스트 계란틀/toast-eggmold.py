from collections import deque

N,L,R = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

stop = False
moved = False

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs(row,col,visited):
    global stop, moved
    q = deque()
    q.append((row,col))
    union = [(row,col)]
    while q:
        now = q.popleft()
        for _ in range(4):
            temp_r = now[0] + dr[_]
            temp_c = now[1] + dc[_]
            if not 0 <= temp_r <N or not 0 <= temp_c < N or visited[temp_r][temp_c]:
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
        new = sum(board[a][b] for a,b in union) // len(union)
        for r,c in union:
            board[r][c] = new

cnt = 0
while not stop:
    moved = False
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == True:
                continue
            visited[r][c] = True
            bfs(r,c,visited)
    if moved : cnt+=1

print(cnt)