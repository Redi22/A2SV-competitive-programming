class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [int(s[:2]) * 60 +  int(s[3:]) for s in timePoints]
        print(minutes)
        minutes.sort()
        min_difference = 1441
        init_min = minutes[0]
        for i in range(1, len(minutes)):
            temp_min = abs(minutes[i] - init_min)
            if(temp_min > 720):
                temp_min = 1440 - temp_min
            if(temp_min < min_difference):
                min_difference = abs(temp_min)
            init_min = minutes[i]
        temp_min = abs(minutes[0] - minutes[len(minutes) - 1] )
        if(temp_min > 720):
                temp_min =  1440 - temp_min
        if(temp_min < min_difference):
            min_difference =temp_min
        return min_difference
        