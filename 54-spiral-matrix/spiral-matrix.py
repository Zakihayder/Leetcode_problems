class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        mat = [row[:] for row in matrix]
    
        while mat:
        # Pop the first row and add it to results
            result.extend(mat.pop(0))
            # Rotate the remaining matrix counter-clockwise
            mat = list(zip(*mat))[::-1]
        
        return result
        