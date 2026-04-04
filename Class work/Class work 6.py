#387
class Solution(object):
    def firstUniqChar(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for i in range(len(s)):
            if count[s[i]]==1:
                return  i
        return -1

#383
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}
        for char in magazine:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in ransomNote:
            if char not in count or count[char]==0:
                return False
            count[char]-=1
        return True

