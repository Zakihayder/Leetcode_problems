class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []          
        current_line = [] 
        line_length = 0   
        
        for word in words:
            if line_length + len(word) + len(current_line) > maxWidth:

                for i in range(maxWidth - line_length):
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                
                res.append("".join(current_line))
                current_line = []
                line_length = 0
                
            current_line.append(word)
            line_length += len(word)
            
        last_line = " ".join(current_line)
        remaining_spaces = maxWidth - len(last_line)
        res.append(last_line + " " * remaining_spaces)
        
        return res
