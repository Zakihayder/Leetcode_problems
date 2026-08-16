class Solution:
    def bagOfTokensScore(self, tokens, power):
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        ans = 0

        while left <= right:

            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                ans = max(ans, score)
                
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1

            else:
                break

        return ans