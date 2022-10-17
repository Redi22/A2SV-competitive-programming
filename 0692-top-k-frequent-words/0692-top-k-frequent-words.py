class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        count the frequency
        insert the frequency with the word in to a max heap
        get the max element at a time
        
        '''
        count = Counter(words)
        heap = []
        kFrequent = []
        
        #insert to the heap
        for word, frequency in count.items():
            heapq.heappush(heap, (-frequency, word))
            
        #collect our k-frequent elements 
        for i in range(k):
            frequentElement = heapq.heappop(heap)
            kFrequent.append(frequentElement[1])
            
        return kFrequent