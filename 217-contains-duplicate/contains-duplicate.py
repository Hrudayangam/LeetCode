# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         count = dict()

#         for element in nums:
#             if element in count:
#                 return True
                
#             else:
#                 count[element] =1 
                
#         return False

class Solution(object):
    def containsDuplicate(self,nums):
        # arr =list(set(nums))
        # if len (arr) == len (nums):
        #     return False
        # else:
        #     return True
        return len(nums) != len(set(nums))