class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp = {}

        for i in s:
            if(i in comp):
                comp[i]+=1
            else:
                comp[i]=1


        for i in t:
            if(i in comp):
                comp[i]-=1
            else:
                return False


        
        for sums in comp.values():
            if(sums!=0):
                return False
        return True