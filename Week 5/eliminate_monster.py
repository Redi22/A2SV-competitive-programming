class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monster_time = [[dist[i],speed[i],dist[i]/speed[i]] for i in range(len(dist))]
        loop_no = 0
        monster_time.sort(key = lambda x: x[2])
        for mt in monster_time:
            mt[0] -= (mt[1] * loop_no)
            if mt[0] > 0:
                loop_no+=1
            else:
                break
        return loop_no