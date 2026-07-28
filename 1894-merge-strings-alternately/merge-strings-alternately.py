class Solution(object):
    def mergeAlternately(self, word1, word2):
        string = ""
        for i in range(min(len(word1),len(word2))):
            string += word1[i]
            string += word2[i]
        
        if len(word1) > len(word2):
            for i in range(len(word2),len(word1)):
                string += word1[i]
        else:
            for i in range(len(word1),len(word2)):
                string += word2[i]

        return string
            

        