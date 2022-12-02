class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count_1 = Counter(word1)
        count_2 = Counter(word2)

        return count_1.keys() == count_2.keys() and sorted(count_1.values()) == sorted(count_2.values()) 