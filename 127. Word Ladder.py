from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque([endWord])
        visited = set([endWord])
        level = 0
        n = len(endWord)
        # if "c" + "g" in "cog":
        #     print("true!")

        def get_neighbors(node):
            res = []
            for i in range(n):
                for a_word in wordList:
                    if node[0:i] in a_word and node[i+1:] in a_word:
                        # print(a_word)
                        res.append(a_word)
            # print(res)
            return res

        def bfs (root, target):
            queue = deque([root])
            # visited = set([root])
            level = 0

            while len(queue) > 0:
                
                for _ in range(len(queue)):
                    node = queue.popleft()
                    visited = set([node]) # in the same level, the node should not be visited twice. 
                    # print(level, node)
                    if node in get_neighbors(target):
                        print("find it", node, level)
                        if target not in wordList:
                            return level + 1
                        else:
                            return level
                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                level += 1
            # print("level", level)
            return level

        wordList.remove(endWord)
        # get_neighbors(endWord)
        return bfs(endWord, beginWord)
