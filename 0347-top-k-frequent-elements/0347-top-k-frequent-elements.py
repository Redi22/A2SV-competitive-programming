class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        kFrequent = []
        
        #count the frequencies
        count = Counter(nums)
        
        #add the frequency and the number tupled in to our max heap
        for num, frequency in count.items():
            heapq.heappush(heap, (-frequency, num))

        #remove the most frequent ones until we reach k
        for i in range(k):
            frequentElement = heapq.heappop(heap)
            kFrequent.append(frequentElement[1])
            
        #return our k-frequent elements
        return kFrequent
        