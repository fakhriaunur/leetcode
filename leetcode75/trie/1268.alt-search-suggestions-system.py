#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

from typing import List


# @lc code=start
class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {}
        self.indices: list[int] = []

    def insert(self, word: str, index: int):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]

            if len(node.indices) < 3:
                node.indices.append(index)

    def search(self, word: str) -> list[list[int]]:
        node = self
        res = [[] for _ in range(len(word))]

        for i, char in enumerate(word):
            if char not in node.children:
                break

            node = node.children[char]
            res[i] = node.indices

        return res


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        trie = Trie()

        for i, word in enumerate(products):
            trie.insert(word, i)

        indices_list = trie.search(searchWord)

        return [
            [products[index] for index in indices_sublist]
            for indices_sublist in indices_list
        ]


# @lc code=end
