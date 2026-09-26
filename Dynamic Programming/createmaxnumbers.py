class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max_subsequence(nums, length):
            stack = []
            remove = len(nums) - length

            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -= 1

                stack.append(num)

            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                # Choose the lexicographically larger remaining sequence
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        answer = []

        # i digits from nums1, k-i digits from nums2
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            part1 = get_max_subsequence(nums1, i)
            part2 = get_max_subsequence(nums2, k - i)

            candidate = merge(part1[:], part2[:])

            if candidate > answer:
                answer = candidate

        return answer
        