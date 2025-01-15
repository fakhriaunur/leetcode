class Trie:
    def __init__(self):
        self.children: dict[str, Trie] = {}
        self.freq = 0

    def insert(self, word: str):
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Trie()

            node = node.children[char]
            node.freq += 1

    def query(self, prefix: str):
        node = self

        for char in prefix:
            if char not in node.children:
                return 0

            node = node.children[char]

            return node.freq
