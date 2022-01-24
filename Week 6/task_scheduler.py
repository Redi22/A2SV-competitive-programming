class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = 0
        waiting = []
        if(n == 0):
            return len(tasks)
        else:
            counted = Counter(tasks)
            my_cou = [[-freq, 0 , val] for val, freq in counted.items()]
            heapq.heapify(my_cou)
            while my_cou or waiting:
                if my_cou:
                    temp = heapq.heappop(my_cou)
                    temp[0] += 1
                    if temp[0] != 0:
                        waiting.append(temp)
                count += 1
                for j in waiting:
                    j[1] += 1
                for j in waiting:
                    if j[1] > n:
                        j[1] = 0
                        waiting.pop(0)
                        heapq.heappush(my_cou , j)
        return count

            
                