class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        counter = 0
        for w in words:
            if x in w: 
                output.append(counter)
            counter += 1
        
        return output