#! /bin/env python3
import operator
import functools
class TrieNode:
    def __init__(self, parent=None):
        self.index_list = []
        self.next = dict()
        self.counter = 0
        self.parent = parent

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.leaves = set()
    
    def add(self, index, s):
        u = self.root
        for e in s:
            if not u.next.get(e, None):
                u.next[e] = TrieNode(u)
            u = u.next[e]
            u.counter += 1
        u.index_list.append(index)
        self.leaves.add(u)

    def get_outter_order(self):
        rt = [[(i, leaf.counter, leaf) for i in leaf.index_list] for leaf in self.leaves]
        rt = functools.reduce(operator.add, rt)
        return sorted(rt, key=lambda x: x[1])

    def travel(self, u):
        for i in u.index_list:
            yield i
        for n in u.next.values():
            yield from self.travel(n)

    def get_inner_order(self, leaf):
        for i in leaf.index_list:
            yield i
        p = leaf.parent
        while p:
            for n in p.next.values():
                if n != leaf:
                    yield from self.travel(n)
            leaf = p
            p = leaf.parent

if __name__ == '__main__':
    trie = Trie()
    trie.add(1, "aba")
    trie.add(2, "aba")
    trie.add(3, "abc")
    x = trie.get_outter_order()
    print(x)

    for i in trie.get_inner_order(x[0][2]):
        print(i)