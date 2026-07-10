class Solution(object):
    def summaryRanges(self, nums):
        
        count = 0
        arr = []
        for i in range(len(nums)):
            if i == len(nums)-1:
                if nums[i] == nums[i-1] + 1:
                    arr.append(str(nums[i-count])+"->"+str(nums[i]))
                else:
                    arr.append(str(nums[i]))
                break
                
            elif nums[i] == nums[i+1] - 1:
                count += 1
                continue
            else:
                if count == 0:
                    arr.append(str(nums[i]))
                else:
                    arr.append(str(nums[i-count])+"->"+str(nums[i]))
                    count = 0
        
        return arr
        