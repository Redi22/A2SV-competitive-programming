class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        ans = set()
        graph = defaultdict(list)
        
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])
        
        for i in range(len(recipes)):
            indegree[recipes[i]] = len(ingredients[i])
            
        queue = deque(supplies)
        
        while queue:
            curr = queue.popleft()
            ans.add(curr)
            for node in graph[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
                
        return [an for an in recipes if an in ans]
             