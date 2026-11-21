class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        stack = [(0, 0, None)]

        while stack:
            node, state, old = stack.pop()

            if state == 0:
                ch = s[node]
                old = last.get(ch, -1)

                if old != -1:
                    new_parent[node] = old

                last[ch] = node

                stack.append((node, 1, old))

                for child in reversed(children[node]):
                    stack.append((child, 0, None))

            else:
                ch = s[node]

                if old == -1:
                    del last[ch]
                else:
                    last[ch] = old

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        for node in reversed(order):
            for child in new_children[node]:
                ans[node] += ans[child]

        return ans

        
        
