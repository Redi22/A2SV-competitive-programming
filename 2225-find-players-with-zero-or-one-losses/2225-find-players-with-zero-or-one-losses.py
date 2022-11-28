class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        played = set()
        for winner, loser in matches:
            losers[loser] += 1
            played.add(winner)
            
            
        answer = [[], []]
        for player in losers:
            if losers[player] == 1:
                answer[1].append(player)
                
        for player in played: 
            if player not in losers:
                answer[0].append(player)
                
        return [sorted(answer[0]), sorted(answer[1])]
        
        