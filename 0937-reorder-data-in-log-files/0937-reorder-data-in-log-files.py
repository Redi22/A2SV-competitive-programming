class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                temp = log.split(' ')
                letters.append((temp[0], " ".join(temp[1:])))
        
        letters.sort(key = lambda x: [x[1],x[0]])
        return [identifier + " " + val for identifier, val in letters] + digits
        