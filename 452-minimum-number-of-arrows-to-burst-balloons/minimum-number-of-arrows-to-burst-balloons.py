class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        # Sort by end coordinate
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        arrow_pos = points[0][1]  # position of first arrow
        
        for start, end in points[1:]:
            if start > arrow_pos:
                # This balloon isn't hit by the current arrow — need a new one
                arrows += 1
                arrow_pos = end
            # else: balloon is already popped by arrow_pos, do nothing
        
        return arrows