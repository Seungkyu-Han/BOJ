import sys
import bisect
from collections import deque

class Node:

    def __init__(self, word: str):
        self.word: str = word
        self.words: list[str] = list()
        self.nodes: list[Node] = list()

    def add_child(self, add_word: str):

        if len(self.words) == 0:
            add_node = Node(add_word)
            self.words.append(add_word)
            self.nodes.append(add_node)
            return add_node

        index = bisect.bisect_left(self.words, add_word)
        if len(self.words) > index and self.words[index] == add_word:
            return self.nodes[index]

        add_node = Node(add_word)

        self.words.insert(index, add_word)
        self.nodes.insert(index, add_node)
        return add_node


class Tree:

    def __init__(self, head: Node):
        self.head = head

    def add_node(self, words: list[str]):
        cur_node = self.head
        for word in words:
            cur_node = cur_node.add_child(word)
        return self.head

    def track(self):
        need_visit = deque()

        for child in self.head.nodes:
            need_visit.append([0, child])

        while need_visit:
            depth, cur = need_visit.popleft()

            print('--' * depth, end='')
            print(cur.word)

            for next_child in reversed(cur.nodes):
                need_visit.appendleft([depth + 1, next_child])



N = int(sys.stdin.readline())

my_tree = Tree(Node(''))

for i in range(N):
    ant_hole = list(sys.stdin.readline().split())[1:]

    my_tree.add_node(ant_hole)

my_tree.track()