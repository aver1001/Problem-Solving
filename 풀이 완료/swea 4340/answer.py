pipe_info = ((),
             ((0, 2), (1, 3)),
             ((0, 2), (1, 3)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2)))
  
dir_list = (0, 1, 2, 3)
  
dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)
  
def bfs():
    global dij
    queue = [[0, 0, 1, 0, set()]]
    while queue:
        r, c, cnt, dir_from, visit = queue.pop(0)
        c_pos = r*N+c
        if c_pos in visit: continue
        pipe = board[r][c]
        if not pipe: continue
        if cnt >= dij[dir_from][r][c]: continue
        if r == N-1 and c == N-1:
            for pipe_dir in pipe_info[pipe]:
                if (dir_from in pipe_dir) and (2 in pipe_dir):
                    dij[dir_from][r][c] = cnt
                    break
            continue
        dij[dir_from][r][c] = cnt
        visit.add(c_pos)
        for pipe_dir in pipe_info[pipe]:
            if dir_from in pipe_dir:
                for p_dir in pipe_dir:
                    if p_dir == dir_from: continue
                    pr, pc = r+dr[p_dir], c+dc[p_dir]
                    if (0 <= pr <= N-1) and (0 <= pc <= N-1):
                        queue.append((pr, pc, cnt+1, dir_list[p_dir-2], visit))
  
  
def bfs2():
    global dij2
    queue = [[N-1, N-1, 1, 2, set()]]
    while queue:
        r, c, cnt, dir_from, visit = queue.pop(0)
        c_pos = r*N+c
        if c_pos in visit: continue
        pipe = board[r][c]
        if not pipe: continue
        if cnt >= dij2[dir_from][r][c]: continue
        if r == 0 and c == 0:
            for pipe_dir in pipe_info[pipe]:
                if (dir_from in pipe_dir) and (0 in pipe_dir):
                    dij2[dir_from][r][c] = cnt
                    break
            continue
        dij2[dir_from][r][c] = cnt
        visit.add(c_pos)
        for pipe_dir in pipe_info[pipe]:
            if dir_from in pipe_dir:
                for p_dir in pipe_dir:
                    if p_dir == dir_from: continue
                    pr, pc = r+dr[p_dir], c+dc[p_dir]
                    if (0 <= pr <= N-1) and (0 <= pc <= N-1):
                        queue.append((pr, pc, cnt+1, dir_list[p_dir-2], visit))
  
  
T = int(input())
switch = 1
for test_case in range(1, T+1):
    N = int(input())
    MAX_VALUE = N*N
    board = tuple(tuple(map(int,input().split())) for _ in range(N))
    dij = [[[MAX_VALUE]*N for _ in range(N)] for x in range(4)]
    bfs()
    ans = MAX_VALUE
    for i in range(4):
        if dij[i][N-1][N-1] < ans: ans = dij[i][N-1][N-1]
    dij2 = [[[MAX_VALUE]*N for _ in range(N)] for x in range(4)]
    bfs2()
    ans2 = MAX_VALUE
    for i in range(4):
        if dij2[i][0][0] < ans2: ans2 = dij2[i][0][0]
    print(f"#{test_case} {min([ans, ans2])}")