class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = [(-value, key) for key, value in count.items()]
        ans = []
        heapq.heapify(count)
        
        while count:
            ch = heapq.heappop(count)
            ans += [(-1 * ch[0]) * ch[1]]
        
        return "".join(ans)