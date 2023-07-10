class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        array = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        array.append(words[i])
        
        return list(set(array))