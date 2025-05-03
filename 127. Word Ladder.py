from collections import deque
from typing import List

### my  not working version:
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


#improved version:
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        
        n = len(endWord)
        wordSet = set(wordList)

        def get_neighbors(word):
            neighbors = []
            for i in range(n):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordSet:
                            neighbors.append(next_word)
            return neighbors

        def bfs(start, target):
            queue = deque([(start, 1)])
            visited = set([start])

            while queue:
                current_word, level = queue.popleft()
                if current_word == target:
                    return level

                for neighbor in get_neighbors(current_word):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
            return 0

        return bfs(endWord, beginWord)

