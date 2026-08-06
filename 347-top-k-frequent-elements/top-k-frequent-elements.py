class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        count = 1
        arr = []

        for i in nums.most_common():
           
            arr.append(i[0])
            if count == k:
                return arr
            count += 1
        

        