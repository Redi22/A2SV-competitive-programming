class Solution:
    def sortSentence(self, s: str) -> str:
        word = ""
        wordSet = {}
        for c in s:
            if(c.isdigit()):
                word +=c
                wordSet[word[-1]] = word[:-1]
                word = ""
            elif(c == ' '):
                continue;
            else:
                word += c
        word = ""
        for i  in sorted(wordSet):
            word += wordSet[i]
            word += " "
        return word[:-1]
        
        