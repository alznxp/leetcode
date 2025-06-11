class Solution:
    def greatestLetter(self, s: str) -> str:
        uppercase = ''
        lowercase = ''
        mySet = set()

        for i in s:
            if i.isupper():
                uppercase = uppercase + i
            else:
                lowercase = lowercase + i

        for j in uppercase:
            if j in lowercase.upper():
                mySet.add(j)
        
        if len(mySet) == 0:
            return ''
        else:
            return max(mySet)