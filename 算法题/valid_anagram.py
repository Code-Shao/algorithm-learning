class Solution:
    def isAnagram(self, s: int, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        for ch in t:
            dict2[ch] = dict2.get(ch, 0) + 1
        print(dict1 == dict2)
        return dict1 == dict2


sol = Solution()
[s, t] = input().split()

if sol.isAnagram(s, t):
    print("valid anagram!")
else:
    print("not valid anagram!")
