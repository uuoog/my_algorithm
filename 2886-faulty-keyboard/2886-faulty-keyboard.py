class Solution:
    def finalString(self, s: str) -> str:
        answer = ""
        for c in s:
            if c == "i":
                answer = answer[::-1]
            else:
                answer +=c
        return answer


