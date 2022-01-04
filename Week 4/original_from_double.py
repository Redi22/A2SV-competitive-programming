class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        cou = Counter(changed)
        res = []
        if (len(changed) % 2 == 0):
            for i  in changed:
                if(cou[i] > 0 and cou[2*i]):
                    if(i != 0):
                        res.append(i)
                        cou[i] -= 1
                        cou[2*i] -= 1
                    elif(cou[i] > 1 ):
                        res.append(i)
                        cou[i] -= 1
                        cou[2*i] -= 1
        return res if len(res) == len(changed) // 2 else [] 