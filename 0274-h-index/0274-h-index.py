class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations = citations[::-1]
        num_pubs = [x+1 for x in range(len(citations))]
        answer = 0
        for citation, num_pub in zip(citations, num_pubs):
            if num_pub >= citation:
                answer = max(answer, citation)
            else:
                answer = num_pub
        return answer
