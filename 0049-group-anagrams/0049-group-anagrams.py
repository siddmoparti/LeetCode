class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = dict()

        for word in strs:
            key = "".join(sorted(word))
        
            if key not in unique:
                unique[key] = []

            unique[key].append(word)
        
        return list(unique.values())



        # sortedWords = sorted(strs)

        # unique = dict()
        # for word in sortedWords:
        #     unique[word] = []
        
        # for word in strs:
        #     key = word.sort()
        #     if key in unique.keys():
        #         unique[key].append(word)
        
        # return unique
            
        


       