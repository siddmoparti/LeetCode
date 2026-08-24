class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        visited.add(beginWord)
        q = collections.deque()
        q.append(beginWord)
        n = len(endWord)

        res = 1
        while q:
            for _ in range(len(q)):

                cur = q.popleft()
                if cur == endWord:
                    return res
                found_next = False
                visited.add(cur)
                for word in wordList:
                    if word in visited:
                        continue
                
                    diff = 0
                    for i in range(n):
                        if word[i] != cur[i]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        visited.add(word)
                        q.append(word)
            res += 1
                        

        return 0
