# class Solution:
#     def isAnagram(self,s,t):
#         if len(s)!= len(t):
#             return False
        
#         count_s,count_t = {},{}

#         for i in range(len(s)):
#             count_s[s[i]] = 1 + count_s.get(s[i],0)
#             count_t[t[i]] = 1 + count_t.get(t[i],0)
#         return count_s == count_t

        




# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        # len_t = 0
        
        # length_s = len(s)
        # length_t = len(t)

        # for i in s:
        #     if i in t:
        #         len_t += 1
        #         if len_t == length_s and length_s == length_t:
        #             return True 

        
# class Solution:
#     def isAnagram(self, s, t):
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT





























class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s={}
        count_t={}

        for i in s:
            if i not in count_s:
                count_s[i] = 1
            # print(count_s)

            else:
                count_s[i] +=1

        for j in t:
            if j not in count_t:
                count_t[j] = 1
            else:
                count_t[j] +=1
        
        if  count_t== count_s:
            return True
        else:
           return False



            

        






