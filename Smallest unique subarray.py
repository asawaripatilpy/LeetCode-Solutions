class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nxt = [{}]
        link = [-1]
        length = [0]
        occ = [0]

        last = 0

        for x in nums:
            cur = len(nxt)

            nxt.append({})
            length.append(length[last] + 1)
            link.append(0)
            occ.append(1)

            p = last

            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0

            else:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q

                else:
                    clone = len(nxt)

                    nxt.append(nxt[q].copy())
                    length.append(length[p] + 1)
                    link.append(link[q])
                    occ.append(0)

                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        # Process states in decreasing length order
        order = sorted(
            range(1, len(nxt)),
            key=length.__getitem__,
            reverse=True
        )

        # Calculate occurrence counts
        for v in order:
            parent = link[v]
            if parent != -1:
                occ[parent] += occ[v]

        # Find the shortest unique substring
        ans = len(nums)

        for v in range(1, len(nxt)):
            if occ[v] == 1:
                ans = min(ans, length[link[v]] + 1)

        return ans
