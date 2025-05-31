class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = [0] * len(boxes)
        for cur in range(len(boxes)):
            if boxes[cur] == "1":
                for new in range(len(boxes)):
                    answer[new] += abs(new - cur)
        return answer