from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        # Courses with no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        while q:
            course = q.popleft()
            order.append(course)

            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []