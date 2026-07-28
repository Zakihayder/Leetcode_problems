from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            word = list(word)

            for i in range(len(word)):
                original = word[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue

                    word[i] = c
                    newWord = "".join(word)

                    if newWord in wordSet:
                        wordSet.remove(newWord)  # mark visited
                        q.append((newWord, steps + 1))

                word[i] = original

        return 0