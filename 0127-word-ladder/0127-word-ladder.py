class Solution:
    def checkDiff(self, base, compare):
        diff = 0
        for i in range(len(base)):
            if base[i] != compare[i]:
                diff += 1
        if diff > 1:
            return False
        else:
            return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # hit
        # #write a func that checks if every word but one word is diff
        # add every word that differs by one letter to a queue
        # hot
        # dot lot
        # dog
        # log cog

        if endWord not in wordList:
            return 0
        
        q = collections.deque()
        visit = set()
        q.appendleft(beginWord)
        visit.add(beginWord)
        res = 1
        
        while q:

            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for w in wordList:
                    if w not in visit:
                        if self.checkDiff(word, w):
                            q.append(w)
                            visit.add(w)
            res += 1
        return 0