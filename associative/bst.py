class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


def find(root, key):

    while root is not None:
        if root.key == key:
            return root
        elif root.key > key:
            root = root.left
        else:
            root = root.right

    return None


def insert(root, key):

    if root is None:
        root = BSTNode(key)
        return root

    p = None
    q = root
    while q is not None:
        if q.key == key:
            return root
        elif q.key > key:
            p = q
            q = q.left
        else:
            p = q
            q = q.right

    node = BSTNode(key)
    if p.key > key:
        p.left = node
        node.parent = p
    else:
        p.right = node
        node.parent = p

    return root


def minval(root):

    p = root
    while p.left is not None:
        p = p.left

    return p


def maxval(root):

    p = root
    while p.right is not None:
        p = p.right

    return p


def remove(root, key):

    p = None
    q = root

    while q is not None:
        if q.key == key:
            break
        elif q.key > key:
            p = q
            q = q.left
        else:
            p = q
            q = q.right

    if q is None:
        return

    if q.left is None and q.right is None:
        if p.left.key == key:
            p.left = None
            return root
        else:
            p.right = None
            return root

    if q.left is not None and q.right is None:
        q.left.parent = p
        if p.left.key == key:
            p.left = q.left
        else:
            p.right = q.left

        return root

    if q.left is None and q.right is not None:
        q.right.parent = p
        if p.left.key == key:
            p.left = q.right
        else:
            p.right = q.right

        return root




