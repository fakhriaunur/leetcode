#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

from typing import Optional
# @lc code=start
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        
        for char in word:
            idx = ord(char) - ord('a')
            
            if not node.children[idx]:
                node.children[idx] = Trie()
            
            node = node.children[idx]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        
        return node is not None
    
    def _search_prefix(self, prefix: str) -> Optional['Trie']:
        node = self
        
        for char in prefix:
            idx = ord(char) - ord('a')
            
            if not node.children[idx]:
                return None
            
            node = node.children[idx]
        
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

