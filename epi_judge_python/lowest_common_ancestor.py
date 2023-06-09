import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
import collections

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    root = None

    def dfs(tree, node0, node1):
        if not tree:
            return False
        nonlocal root

        left = dfs(tree.left, node0, node1)
        right = dfs(tree.right, node0, node1)
                
        if (left and right) or ((left or right) 
                                and (tree.data == node0.data or tree.data == node1.data)) or (tree.data == node0.data and tree.data == node1.data):
            root = tree
            return True
        
        # Bug1
        # Code: return left or right 
        #
        # - forgot to check current node value, we are using postorder traversal
        # - if node.data = tree.data, also we return True
        # - After we return (pop), we can't visit this node again in the future

        # Fix bug1
        return left or right or tree.data == node0.data or tree.data == node1.data

    dfs(tree, node0, node1)
    return root

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
