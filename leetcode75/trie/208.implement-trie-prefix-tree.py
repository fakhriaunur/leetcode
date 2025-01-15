#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start


class Trie:
    def __init__(self):
        self.children: dict[int, Trie] = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            index = ord(char) - ord("a")
            if index not in node.children:
                node.children[index] = Trie()

            node = node.children[index]

        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)

        return node is not None and node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)

        return node is not None

    def _search_prefix(self, prefix: str):
        node = self

        for char in prefix:
            index = ord(char) - ord("a")
            if index not in node.children:
                return None

            node = node.children[index]

        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
