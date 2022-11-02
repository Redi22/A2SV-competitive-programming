class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(0, start)])
        visited = set()
        genes = ['A', 'C', 'G', 'T']
        bank.append(start)
        bank_set = set(bank)
        
        while queue:
            step, variant = queue.popleft()
            
            if variant in visited or variant not in bank_set:
                continue
                
            if variant == end:
                return step
            
            visited.add(variant)
            
            for i in range(len(variant)):
                for single_gene in genes:
                    new_variant = variant[:i] + single_gene + variant[i + 1:]
                    queue.append((step + 1, new_variant))
                    
                    
        return -1
                    