class Solution:
    def groupAnagrams(self, strs):
        AmanList = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in AmanList:
                AmanList[key] = []

            AmanList[key].append(word)

        return list(AmanList.values())
               
