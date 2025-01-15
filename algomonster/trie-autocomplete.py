class Node:
    def __init__(self, value: str):
        self.children: dict[str, Node] = {}
        self.value = value
        self.freq = 0

    def insert(self, s: str, idx: int):
        self.freq += 1

        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx])).insert(s, idx + 1)

    def query(self, s: str, idx: int) -> int:
        if idx == len(s) or self.freq == 1:
            return 0

        return self.children[s[idx]].query(s, idx + 1) + 1


def autocomplete(words: list[str]) -> int:
    trie = Node("$")
    total = 0

    for word in words:
        trie.insert(word, 0)
        total += trie.query(word, 0)

    return total + 1
