class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in strs:
            sort = sorted(i)
            word = ""
            for j in sort:
                word += j
            print(word)
            if word in d:
                d[word].append(i)
            else:
                d[word] = [i]
        
        for val in d.values():
            ans.append(val)
        return ans