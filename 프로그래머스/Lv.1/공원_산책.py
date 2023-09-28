def solution(park, routes):
    # 시작 위치
    for i in range(len(park)):
        for j in range(len(park[i])):
            if (park[i][j] == 'S'):
                x, y = j, i
                
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for s in routes:
        op, n = s.split()
        if (op == 'N'): 
            nx, ny = dx[0], dy[0]
        elif (op == 'S'): 
            nx, ny = dx[1], dy[1]
        elif (op == 'W'):
            nx, ny = dx[2], dy[2]
        else:
            nx, ny = dx[3], dy[3]
        flag = True
        for i in range(1, int(n) + 1):
            xx = x + nx * i
            yy = y + ny * i
            if (xx < 0 or xx >= len(park[0]) or yy < 0 or yy >= len(park) or park[yy][xx] == 'X'):
                flag = False
                break
        if (flag): 
            x, y = x + nx * int(n), y + ny * int(n)
                
    answer = [y, x]
    return answer
