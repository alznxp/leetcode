class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        unique_integers = set()
        n = len(digits)

        for p in permutations(digits, 3):
            if p[0] == 0:
                continue

            if p[2] % 2 == 0:
                unique_integers.add(int("".join(map(str, p))))
        
        return sorted(list(unique_integers))