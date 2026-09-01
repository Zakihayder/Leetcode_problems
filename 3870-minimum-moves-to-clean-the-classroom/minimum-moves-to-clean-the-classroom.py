class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
    
        m, n = len(classroom), len(classroom[0])

        litter = {}
        sr = sc = 0
        litter_count = 0

        # Find start and assign each litter a bit
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = litter_count
                    litter_count += 1

        # No litter
        if litter_count == 0:
            return 0

        target = (1 << litter_count) - 1

        # (row, col, energy, mask)
        q = deque([(sr, sc, energy, 0)])

        # Store states already visited
        visited = {(sr, sc, energy, 0)}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Outside grid / obstacle
                    if (
                        nr < 0 or nr >= m or
                        nc < 0 or nc >= n or
                        classroom[nr][nc] == 'X'
                    ):
                        continue

                    # Moving costs 1 energy
                    ne = e - 1

                    # Cannot move with zero energy unless
                    # the destination is a reset area.
                    if ne < 0:
                        continue

                    # Collect litter
                    nmask = mask

                    if classroom[nr][nc] == 'L':
                        bit = litter[(nr, nc)]
                        nmask |= 1 << bit

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, nmask)

                    if state not in visited:
                        visited.add(state)
                        q.append(state)

            moves += 1

        return -1