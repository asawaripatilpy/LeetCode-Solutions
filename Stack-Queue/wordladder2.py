class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]: 
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        parents = defaultdict(list)
        current = {beginWord}
        found = False

        while current and not found:
            word_set -= current
            next_level = set()

            for word in current:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in word_set:
                            next_level.add(new_word)
                            parents[new_word].append(word)

            if endWord in next_level:
                found = True

            current = next_level

        if not found:
            return []

        result = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return result
        