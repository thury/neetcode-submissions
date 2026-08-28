class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqDict = {}
        for string in strs:
            freq = []
            for char in string:
                freq.append(char)
            freq.sort()
            freqStr = ''.join(freq)
            if freqStr in freqDict:
                freqDict[freqStr].append(string)
            else:
                newList = [string]
                freqDict[freqStr] = newList
        answer = []
        for key in freqDict.keys():
            answer.append(freqDict[key])
        return answer
                