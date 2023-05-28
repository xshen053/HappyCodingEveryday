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
        nonlocal root
        if not tree:
            return False

        left = dfs(tree.left, node0, node1)
        right = dfs(tree.right, node0, node1)
        # this if statement includes 3 cases
        # 1. two nodes are in two subtrees
        # 2. one node is tree node, the other in one of subtree
        # 3. two nodes are both tree node, (1, 1, 1)

        if ((left and right) 
            or ((tree.data == node0.data 
                 or tree.data == node1.data) 
                 and (left or right)) 
                 or (tree.data == node0.data 
                     and node0.data == node1.data)):
            root = tree
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
