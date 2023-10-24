

# class Solution(object):
#     def twoSum(self, nums, target):
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
#             print(prevMap)

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

            

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#     #    seen

#        '''
#          logic:
#          * first element lege, if it is less than the target, aage jayege
#          * if i + (i+1) != target continue
#          * if match, add in set
         
#        '''



#        ans = 




























