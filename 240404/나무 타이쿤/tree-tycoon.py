N,M = list(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
rule_per_year = [list(map(int,input().split())) for _ in range(M)]
pos = [(N-2,0),(N-2,1),(N-1,0),(N-1,1)]
dr = [0,-1,-1,-1,0,1,1,1]
dc = [1,1,0,-1,-1,-1,0,1]
dcross_r = [-1,1,-1,1]
dcross_c = [-1,-1,1,1]
#1
def move(rule):
    direction, num = rule
    for _ in range(len(pos)):
        new_r,new_c = pos[_][0]+(dr[direction-1]*num), pos[_][1]+(dc[direction-1]*num)
        new_r = new_r - N if new_r > N-1 else new_r
        new_c = new_c - N if new_c > N-1 else new_c
        new_r = new_r + N if new_r < 0 else new_r
        new_c = new_c + N if new_c < 0 else new_c
        pos[_] = (new_r,new_c)

#2~3
def inject():
    global pos
    growup = []
    for _ in pos:
        board[_[0]][_[1]] += 1
    for idx in range(len(pos)):
        row,col = pos[idx]
        cnt = 0
        for _ in range(4):
            search_r, search_c = row + dcross_r[_], col + dcross_c[_]
            if not 0 <= search_r <= N-1 or not 0 <= search_c <= N-1:
                continue
            cnt += 1 if board[search_r][search_c] >= 1 else 0
        growup.append(cnt)
    for _ in range(len(pos)):
        row,col = pos[_]
        board[row][col] += growup[_]
        

#4
def cut():
    global pos
    temp = []
    for row in range(N):
        for col in range(N):
            if board[row][col] < 2 or (row,col) in pos:
                continue
            board[row][col] -= 2
            temp.append((row,col))
    pos = temp


for _ in range(M):
    move(rule_per_year[_])
    inject()
    cut()
    
temp = 0
for _ in board:
    temp += sum(_)
print(temp)