from collections import deque

class Solution:
    def catMouseGame(self, graph):
        n = len(graph)

        result = [[[0, 0] for _ in range(n)] for _ in range(n)]

        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]

        MOUSE = 0
        CAT = 1

        MOUSE_WIN = 1
        CAT_WIN = 2

        q = deque()

        for m in range(n):
            for c in range(1, n):
                degree[m][c][MOUSE] = len(graph[m])

                degree[m][c][CAT] = sum(x != 0 for x in graph[c])

        for c in range(1, n):
            for turn in range(2):
                result[0][c][turn] = MOUSE_WIN
                q.append((0, c, turn))

        for x in range(1, n):
            for turn in range(2):
                result[x][x][turn] = CAT_WIN
                q.append((x, x, turn))

        while q:
            m, c, turn = q.popleft()
            winner = result[m][c][turn]

            prev_turn = turn ^ 1

            if prev_turn == MOUSE:
                for prev_m in graph[m]:
                    pm, pc = prev_m, c

                    if result[pm][pc][prev_turn] != 0:
                        continue

                    if winner == MOUSE_WIN:
                        result[pm][pc][prev_turn] = MOUSE_WIN
                        q.append((pm, pc, prev_turn))

                    else:
                        degree[pm][pc][prev_turn] -= 1

                        if degree[pm][pc][prev_turn] == 0:
                            result[pm][pc][prev_turn] = CAT_WIN
                            q.append((pm, pc, prev_turn))

            else:
                for prev_c in graph[c]:

                    if prev_c == 0:
                        continue

                    pm, pc = m, prev_c

                    if result[pm][pc][prev_turn] != 0:
                        continue

                    if winner == CAT_WIN:
                        result[pm][pc][prev_turn] = CAT_WIN
                        q.append((pm, pc, prev_turn))

                    else:
                        degree[pm][pc][prev_turn] -= 1

                        if degree[pm][pc][prev_turn] == 0:
                            result[pm][pc][prev_turn] = MOUSE_WIN
                            q.append((pm, pc, prev_turn))

        return result[1][2][MOUSE]