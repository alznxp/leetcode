from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits_counter = Counter(map(str,digits))

        def isPossible(n):
            num = Counter(str(n))
            return num == (num & digits_counter)

        output = list(filter(isPossible, range(100,1000,2)))

        return output