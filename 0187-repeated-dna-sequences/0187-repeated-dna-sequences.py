class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        super_set = set()
        n = len(s)

        #building a super set
        for i in range(n - 9):
            current_sequence = s[i:i + 10]

            #check for mulitple elements
            if current_sequence in super_set:
                result.add(current_sequence)
            super_set.add(current_sequence)

        return result
        