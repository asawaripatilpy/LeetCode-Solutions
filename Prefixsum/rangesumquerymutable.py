class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

        

    def update(self, index: int, val: int) -> None:
        pos = self.n + index
        self.tree[pos] = val

        pos //= 2

        while pos >= 1:
            self.tree[pos] = (
                self.tree[2 * pos] + self.tree[2 * pos + 1]
            )
            pos //= 2

        

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n

        result = 0

        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1

            if right % 2 == 0:
                result += self.tree[right]
                right -= 1

            left //= 2
            right //= 2

        return result
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)