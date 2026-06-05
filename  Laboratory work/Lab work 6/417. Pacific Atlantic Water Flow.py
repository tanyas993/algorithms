class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        tih = set()
        atl = set()
        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, visit)
        for c in range(cols):
            dfs(0, c, tih)
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, 0, tih)
            dfs(r, cols - 1, atl)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in tih and (r, c) in atl:
                    res.append([r, c])

        return res