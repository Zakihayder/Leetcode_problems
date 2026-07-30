class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word) < 9:
            return len(word)
        elif len(word) < 17:
            return 8+(len(word)-8)*2
        elif len(word) < 25:
            return 24+(len(word)-16)*3
        else:
            return 48+(len(word)-24)*4

        