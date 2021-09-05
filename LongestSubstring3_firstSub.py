#%%
class Solution:
    def lengthOfLongestSubstring(self, s):
        n = []
        maxL = []
        
        for i in range(0,len(s)):
            tmp = s[i]
            if tmp not in n and i != len(s)-1:
                n.append(tmp)
                
            elif tmp not in n and i == len(s)-1:
                n.append(tmp)
                maxL.append(len(n))
            else:
                maxL.append(len(n))
                n = n[n.index(tmp)+1:]
                n.append(tmp)
        if maxL == [] and len(s) == 0:
            return 0
        elif maxL == [] and len(s)>0:
            return len(s)
        else:
            maxLL = max(maxL)
            return maxLL
# %%
sIns = Solution()
# %%
sIns.lengthOfLongestSubstring('dvdf')
