class Solution:
    def minimumPushes(self, word: str) -> int:
        word1 = Counter(word)
        total = 0
        for index,(word,count) in enumerate(word1.most_common()):
            if index < 8:
                total += count
            elif index < 16:
                total += count*2
            elif index < 24:
                total += count*3
            else:
                total += count*4
        return total