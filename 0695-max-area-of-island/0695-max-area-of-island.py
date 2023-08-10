class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque

        answer = 0
        visited = set()
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 1. (i, j)가 이미 방문한 위치라면 continue
                if (i, j) in visited:
                    continue
                # 2. grid 상의 값이 0이면 continue
                if grid[i][j] == 0:
                    continue
                # 3. 방문하지 않았고, grid 상의 값이 1이면 BFS
                q = deque([(i, j)])
                area = 0
                while q:
                    cur_y, cur_x = q.popleft()
                    # 꺼내온 좌표가 이미 방문한 좌표인지 아닌지 체크
                    if (cur_y, cur_x) in visited:
                        continue
                    # 만약 유효한 좌표라면 image에서 색상을 바꿔줄 것
                    visited.add((cur_y, cur_x))
                    # 섬의 넓이를 구하는 로직
                    area += 1
                    # 이동할 좌표 계산, 이동 가능한지 체크하고, 큐에 넣어줌
                    for move in moves:
                        new_y, new_x = cur_y + move[0], cur_x + move[1]
                        if new_y < 0 or new_y > len(grid) - 1:
                            continue
                        if new_x < 0 or new_x > len(grid[0]) - 1:
                            continue
                        if grid[new_y][new_x] == 1:
                            q.append((new_y, new_x))
                # 4. 섬의 넓이와 answer 중 더 큰값을 answer로 지정
                answer = max(answer, area)
        return answer