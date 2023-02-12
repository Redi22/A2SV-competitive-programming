class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    	# Build the graph, since it is undirected, we add both directions
        graph = defaultdict(list)
        for c1,c2 in roads:
            graph[c1].append(c2)
            graph[c2].append(c1)
        
        # The total fuel needed, it will be updated in the dfs.
        res = 0

        # The graph has no cycles, but it is undirected, 
        # so we need to pass in the paraent node here to make sure it is not traveling backward.
        def dfs(node,par):
            nonlocal res
            # Count how many people arrived at the current node.
            # Start with 1 because each node initially has one people.
            totalPeople = 1

            for nei in graph[node]:
            	# Make sure to not travel backward.
                if nei != par:

                    people, car = dfs(nei,node)
                    
                    # Adding the people arraving the current node
                    totalPeople += people
                    
                    # Add the number of cars going from the neighbor node to the current node to the result
                    # Since each car traveled on edge, number of cars == number of fuel used
                    res += car

            # Based on the number of people arrived at the current node, we can calcualte the cars actually needed.
            # In other words, we try to rearrange the people in the minimum number of cars possible bease on the seats each car has.
            cars = ceil(totalPeople/seats)
            
            # If this is at a leaf node, totalPeople=1, and cars=1 
            return totalPeople,cars

        dfs(0,None)
        return res