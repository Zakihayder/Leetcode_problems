class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque([id])
        visited = {id}

        for _ in range(level):
            for _ in range(len(q)):
                person = q.popleft()

                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        q.append(friend)

        count = Counter()

        for person in q:
            for video in watchedVideos[person]:
                count[video] += 1

        return sorted(count, key=lambda video: (count[video], video))