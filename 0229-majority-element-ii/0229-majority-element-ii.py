class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        answer = []
        counter = Counter(nums)
        for key, count in counter.items():
            if counter[key] > len(nums)/3:
                answer.append(key)
        return answer
