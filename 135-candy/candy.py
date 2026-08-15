class Solution:
    def candy(self, ratings):
        n = len(ratings)

        if n <= 1:
            return n

        def triangle(x):
            return x * (x + 1) // 2

        ans = 0
        up = 0
        down = 0
        prev_slope = 0

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                slope = 1
            elif ratings[i] < ratings[i - 1]:
                slope = -1
            else:
                slope = 0

            if (prev_slope > 0 and slope == 0) or \
               (prev_slope < 0 and slope >= 0):

                ans += triangle(up) + triangle(down) + max(up, down)

                up = 0
                down = 0

            if slope > 0:
                up += 1
            elif slope < 0:
                down += 1
            else:
                ans += 1

            prev_slope = slope

        ans += triangle(up) + triangle(down) + max(up, down) + 1

        return ans