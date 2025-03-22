"""

Resultados:

Tempo na busca Trie: 3.743171691894531e-05
Tempo na busca linear: 0.00025177001953125

Comparando o tempo gastado de cada algoritmo, a busca Trie se provou mais rápida e mais eficiente do que a busca linear.

"""

import random
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):

        def _delete(node, word, depth): # Auxiliary.
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]

            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete(self.root, word, 0)

    def longest_common(self, query):
        node = self.root

        longest = ""
        current = ""

        for i in query:
            if i in node.children:
                current += i
                node = node.children[i]
                if node.is_end_of_word:
                    longest = current
            else:
                longest = current
                break

        return longest

    def list_words(self):
        
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words

trie = Trie()

def generate_ipv4():
    return "{}".format(".".join(str(random.randint(0, 255)) for _ in range(4)))

def generate_ipv4_list(count=999):
    return [generate_ipv4() for _ in range(count)]

ipv4_list = generate_ipv4_list()

ipv4_list.append("192.168.1.55")

ipToBeFound = "192.168.1.55"

for i in ipv4_list:
    trie.insert(i)

def longest_prefix_linear(lst, ipToBeFound):
    longest = ""
    max_match = -1

    for ip in lst:
        ip_prefix = ip.split("/")[0]
        size = 0

        for idx in range(min(len(ip_prefix), len(ipToBeFound))):
            if ip_prefix[idx] == ipToBeFound[idx]:
                size += 1
            else:
                break

    if size > max_match:
        max_match = size
        longest = ip

    return longest

start = time.time()
print(trie.longest_common(ipToBeFound))
end = time.time()

print(f"Tempo na busca Trie: {end - start}")

start = time.time()
print(longest_prefix_linear(ipv4_list, ipToBeFound))
end = time.time()

print(f"Tempo na busca linear: {end - start}")