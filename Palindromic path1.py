class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        
        word_map = {word: i for i, word in enumerate(words)}
        result = set()

        def isPalindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):

            for j in range(len(word) + 1):

                prefix = word[:j]
                suffix = word[j:]

                rev_prefix = prefix[::-1]
                rev_suffix = suffix[::-1]

                # Case 1: Prefix is palindrome
                if isPalindrome(prefix):
                    if rev_suffix in word_map:
                        k = word_map[rev_suffix]

                        if k != i:
                            result.add((k, i))

                # Case 2: Suffix is palindrome
                if isPalindrome(suffix):
                    if rev_prefix in word_map:
                        k = word_map[rev_prefix]

                        if k != i:
                            result.add((i, k))
        return [list(pair) for pair in result]                  
