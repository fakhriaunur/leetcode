class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children: dict[str, Node] = {}
        self.freq = 0

    def insert(self, s: str, idx: int) -> None:
        self.freq += 1

        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx])).insert(s, idx + 1)

    def prefix_check(self, s: str, idx: int) -> int:
        if idx == len(s):
            return self.freq

        if s[idx] in self.children:
            return self.children[s[idx]].prefix_check(s, idx + 1)

        else:
            return 0


def prefix_count(words: list[str], prefixes: list[str]) -> list[int]:
    trie = Node("$")

    for word in words:
        trie.insert(word, 0)

    ans = []

    for prefix in prefixes:
        ans.append(trie.prefix_check(prefix, 0))

    return ans
