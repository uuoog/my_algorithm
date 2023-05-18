class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_list = []
        final_score = 0
        for i in range(len(operations)):
            if operations[i] not in ["C", "D", "+"]:
                score_list.append(int(operations[i]))
            if operations[i] == "+":
                score_list.append(score_list[len(score_list)-1] + score_list[len(score_list)-2])
            if operations[i] == "D":
                score_list.append(score_list[len(score_list)-1] * 2)
            if operations[i] == "C":
                score_list.pop()
        final_score = sum(score_list)
        return final_score