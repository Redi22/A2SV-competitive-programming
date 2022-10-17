class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = Counter(sentence)
        return all([i in count for i in 'abcdefghijklmnopqrstuvwxyz'])