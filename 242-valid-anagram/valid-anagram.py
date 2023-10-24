class Solution:
    def isAnagram(self,s,t):
        if len(s)!= len(t):
            return False
        
        count_s,count_t = {},{}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        return count_s == count_t

    





# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         count_s={}
#         count_t={}

#         for i in s:
#             if i not in count_s:
#                 count_s[i] = 1
#             # print(count_s)

#             else:
#                 count_s[i] +=1

#         for j in t:
#             if j not in count_t:
#                 count_t[j] = 1
#             else:
#                 count_t[j] +=1
        
#         if  count_t== count_s:
#             return True
#         else:
#            return False



            

        






