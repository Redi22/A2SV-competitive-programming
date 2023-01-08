class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:        
        if sum(gas) < sum(cost): return -1
        tank = indx = 0
        for i in range(len(gas)):
            tank+= gas[i] - cost[i]
            if tank < 0: tank, indx = 0, i + 1
        return indx