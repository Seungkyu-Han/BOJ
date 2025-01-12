import sys

sys.setrecursionlimit(10 ** 6)

def solution(nodeinfo):

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    nodeinfo.sort(key=lambda x: x[1], reverse=True)

    start_node = Node(index=nodeinfo[0][2], x=nodeinfo[0][0], y=nodeinfo[0][1])

    for info_node in nodeinfo[1:]:
        this_node = Node(index=info_node[2], x=info_node[0], y=info_node[1])

        add(start_node, this_node)

    return [pre(start_node), suf(start_node)]

def add(head_node, added_node):
    
    if head_node.x > added_node.x:
        if head_node.left == None:
            head_node.left = added_node
        else:
            add(head_node.left, added_node)
    else:
        if head_node.right == None:
            head_node.right = added_node
        else:
            add(head_node.right, added_node)


class Node:

    def __init__(self, index, x, y, left=None, right=None):
        self.index = index
        self.left = left
        self.right = right
        self.x = x
        self.y = y


def pre(node):
    result = []
    result.append(node.index)
    
    if node.left != None:
        result += pre(node.left)
    if node.right != None:
        result += pre(node.right)
    return result
    

def suf(node):
    result = []
    
    if node.left != None:
        result += suf(node.left)
    if node.right != None:
        result += suf(node.right)
    return result + [node.index]