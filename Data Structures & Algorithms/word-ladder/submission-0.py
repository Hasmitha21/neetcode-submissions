class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        

        n = len(wordList)
        m = len(wordList[0])
        adj = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        q = collections.deque([beginWord])
        path = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return path
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in adj[pattern]:
                        if neiword not in visited:
                            visited.add(neiword)
                            q.append(neiword)


            path += 1
        
        return 0

        
