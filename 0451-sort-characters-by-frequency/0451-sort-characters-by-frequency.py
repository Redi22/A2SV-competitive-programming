class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        count the characters and store their frequency
        have a max heap and construct the new word by popping from the heap
        '''
        
        heap = []
        count = Counter(s)
        resultString = []
        
        #for each character insert to the heap
        for char, frequency in count.items():
            heapq.heappush(heap, (-frequency, char))
            
            
        while heap:
            current = heapq.heappop(heap)
            resultString.append(current[1] * -current[0])
            
        return "".join(resultString)