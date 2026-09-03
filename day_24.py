# Trees
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right = TreeNode(15)

def preorder(root):
    if root is None:
        return

    print(root.value)
    preorder(root.left)
    preorder(root.right)

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()

        print(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

def find_max(root):
    if root is None:
        return float("-inf")

    left_max = find_max(root.left)
    right_max = find_max(root.right)

    return max(root.value, left_max, right_max)

def count_nodes(root):
    if root is None:
        return 0

    left = count_nodes(root.left)
    right = count_nodes(root.right)

    return 1 + left + right

def sum_nodes(root):
    if root is None:
        return 0

    left = sum_nodes(root.left)
    right = sum_nodes(root.right)

    return root.value + left + right

def height(root):
    if root is None:
        return -1

    left = height(root.left)
    right = height(root.right)

    return 1 + max(left, right)

def count_leaves(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left = count_leaves(root.left)
    right = count_leaves(root.right)

    return left + right

def search(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    left = search(root.left, target)
    right = search(root.right, target)

    return left or right

def bst_search(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    if target < root.value:
        return bst_search(root.left, target)

    return bst_search(root.right, target)

def find_min(root):
    if root.left is None:
        return root

    return find_min(root.left)

def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)

    elif value > root.value:
        root.right = delete(root.right, value)

    else:
        # No left child
        if root.left is None:
            return root.right

        # No right child
        if root.right is None:
            return root.left

        # Two children
        successor = find_min(root.right)
        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root

def is_valid_bst(root, min_val, max_val):
    if root is None:
        return True

    if root.value <= min_val or root.value >= max_val:
        return False

    return (
        is_valid_bst(root.left, min_val, root.value)
        and
        is_valid_bst(root.right, root.value, max_val)
    )

def check_height(root):
    if root is None:
        return 0

    left = check_height(root.left)

    if left == -1:
        return -1

    right = check_height(root.right)

    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return 1 + max(left, right)

def is_balanced(root):
    return check_height(root) != -1

def has_path_sum(root, target):
    if root is None:
        return False

    if target == root.value and root.left is None and root.right is None:
        return True

    return (
        has_path_sum(root.left, target - root.value)
        or
        has_path_sum(root.right, target - root.value)
    )

def diameter(root):
    result = [0]

    def height(root):
        if root is None:
            return -1

        left = height(root.left)
        right = height(root.right)

        result[0] = max(result[0], left + right + 2)

        return 1 + max(left, right)

    height(root)
    return result[0]

def build_tree(preorder, inorder):
    if not preorder:
        return None

    root_value = preorder[0]
    root = TreeNode(root_value)

    root_index = inorder.index(root_value)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_count = len(left_inorder)

    left_preorder = preorder[1:left_count + 1]
    right_preorder = preorder[left_count + 1:]

    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)

    return root

print(diameter(root))