#%%
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        sign = 1 if x>=0 else -1
        unsignedx = abs(x)
        while unsignedx != 0:
            pop = unsignedx % 10
            unsignedx //= 10
            if rev < 2**31//10 or (rev == 2**31//10 and pop <= 7 and sign == 1) or (rev == 2**31//10 and pop <= 8 and sign == -1):
                rev = rev*10+pop
            else:
                return 0
        return sign*rev

# %%
solutionInstance = Solution()
solutionInstance.reverse(123)
