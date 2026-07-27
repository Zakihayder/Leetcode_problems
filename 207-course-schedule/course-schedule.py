from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        # Start with courses having no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        taken = 0

        while q:
            course = q.popleft()
            taken += 1

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return taken == numCourses