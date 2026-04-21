class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict1 = {}
        myDict2 = {}
        for i in s:
            myDict1[i] = myDict1.get(i, 0)+1
        for i in t:
            myDict2[i] = myDict2.get(i, 0)+1

        return myDict1==myDict2 
        

