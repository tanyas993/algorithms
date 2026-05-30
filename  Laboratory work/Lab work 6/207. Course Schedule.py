class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1: return False
            if state[node] == 2: return True

            state[node] = 1
            for n in graph[node]:
                if not dfs(n):
                    return False
            state[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))