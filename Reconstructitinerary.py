class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)

        # Build graph in reverse alphabetical order
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]

        
