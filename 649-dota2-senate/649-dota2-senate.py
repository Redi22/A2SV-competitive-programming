class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rSenates = deque()
        dSenates = deque()
        senateNum = len(senate)
        
        for i in range(senateNum):
            if senate[i] == "R":
                rSenates.append(i)
            else:
                dSenates.append(i)
        while dSenates and rSenates:
            currD = dSenates.popleft() 
            currR = rSenates.popleft()
            if currD < currR:
                dSenates.append(senateNum + currD)
            else:
                rSenates.append(senateNum + currR)
        if dSenates:
            return "Dire"
        return "Radiant"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(senate)
        # votingQueue = deque([i for i in senate])
        # countPopped = 0
        # while votingQueue:
        #     countPopped = 0
        #     votes = Counter(votingQueue)
        #     current = votingQueue.popleft()
        #     if len(votingQueue) - votes[current] <= 0:
        #         if current == "R":
        #             return "Radiant"
        #         return "Dire"
        #     while votingQueue and  votingQueue.popleft() == current:
        #         countPopped += 1
        #     for i in range(countPopped):
        #         votingQueue.appendleft(current)
        #     votingQueue.append(current)
        