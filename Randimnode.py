# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

        

    def getRandom(self):
        """
        :rtype: int
        """
        curr = self.head
        result = None
        count = 0

        while curr:
            count += 1

            if random.randint(1, count) == 1:
                result = curr.val

            curr = curr.next

        return result
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
