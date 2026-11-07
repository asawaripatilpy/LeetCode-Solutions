class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            result.append(index)

            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return result

        
