
class Node(object):
    v = None
    p = None
    n = None

    def __init__(self, v):
        self.v = v

class LL(object):
    head = None
    tail = None

    count = 0

    def __init__(self, arr):
        self.count = len(arr)
        self.head = Node(arr[0])

        cur = self.head

        for i,item in enumerate(arr):
            if i == 0: continue

            nxt = Node(item)
            cur.n = nxt
            nxt.p = cur

            cur = nxt

        self.tail = cur

    def ring_nxt(self, node):
        if node.n:
            return node.n
        else:
            return self.head

    def ring_prv(self, node):
        if node.p:
            return node.p
        else:
            return self.tail

    def nth(self, n):
        node = self.head
        for i in range(n):
            node = node.n
        return node

    def to_iter(self):
        node = self.head
        while node != None:
            yield node.v
            node = node.n

    def rm_node(self, node):
        if node == self.head:
            self.head = node.n
        if node == self.tail:
            self.tail = node.p

        if node.p:
            node.p.n = node.n
        if node.n:
            node.n.p = node.p
        self.count -= 1

    # inserts newnode after node
    def ins_node_after(self, node, newnode):
        newnode.p = node
        if node.n:
            node.n.p = newnode
        newnode.n = node.n
        node.n = newnode

        if node == self.tail:
            self.tail = newnode

        self.count += 1

    # inserts newnode before node
    def ins_node_before(self, node, newnode):
        newnode.n = node
        if node.p:
            node.p.n = newnode
        newnode.p = node.p
        node.p = newnode

        if node == self.head:
            self.head = newnode

        self.count += 1


