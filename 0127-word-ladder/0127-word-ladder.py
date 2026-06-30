class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. Convert list to a set for O(1) lookups and tracking visits
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        q = collections.deque([beginWord])
        res = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return res
                
                # 2. Generate neighbors by mutating the word, instead of looping wordList
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        
                        # If it's a valid unvisited word, queue it
                        if next_word in word_set:
                            q.append(next_word)
                            word_set.remove(next_word) # Removing replaces the "visit" set
            res += 1

        return 0