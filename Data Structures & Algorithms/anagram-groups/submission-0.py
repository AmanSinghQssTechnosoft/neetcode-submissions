from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        AmanList = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in AmanList:
                AmanList[key] = []

            AmanList[key].append(word)

        return list(AmanList.values())
               
