class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = collections.deque()
        q.append(beginWord)
        n = len(endWord)
        res = 0
        visited = set()
        visited.add(beginWord)
        while q:
            res += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for w in wordList:
                    diff = 0
                    for i in range(n):
                        if w[i] != word[i]:
                            diff += 1
                        if diff > 1:
                            break
                    
                    if diff == 1 and w not in visited:
                        visited.add(w)
                        q.append(w)

        return 0
        # hit->hot->dot,lot->dog,log->cog
        
        
        
                
        