from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    
    def helper(p: BinaryTreeNode, q:BinaryTreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (p.data == q.data 
                    and helper(p.left, q.right) 
                    and helper(p.right, q.left))

    return not tree or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
