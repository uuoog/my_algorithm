class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        answer = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                answer += 1
        return answer
