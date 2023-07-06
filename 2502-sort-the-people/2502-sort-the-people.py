class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for i in range(len(names)):
            l.append([heights[i], names[i]])
        l = sorted(l, reverse=True)
        return [name for height, name in l]
