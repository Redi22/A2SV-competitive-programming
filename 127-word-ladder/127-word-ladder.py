class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        variation = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                variate = word[:i]+'*'+word[i+1:]
                variation[variate].append(word)
               
        visited  = set()
        queue = deque([(beginWord, 1)])
        while queue:
            cur = queue.popleft()
            if cur[0] not in visited:
                visited.add(cur[0])

                if cur[0] == endWord:
                    return cur[1]

                for i in range(len(cur[0])):
                    variate = cur[0][:i]+'*'+ cur[0][i+1:]
                    for el in variation[variate]:
                        if el not in visited:
                            queue.append((el,cur[1] + 1))

        return 0