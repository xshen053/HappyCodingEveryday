from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result: List[List[int]] = []
    # STEP 1: What if tree is None
    if not tree:
        return result
    
    cur_depth_nodes = [tree]

    # {inv: all nodes of the tree whose root is cur_d_n + nodes in result = pre_tree}
    while cur_depth_nodes:
        # append a list, don't forget []
        result.append([curr.data for curr in cur_depth_nodes])
        cur_depth_nodes = [
            child for curr in cur_depth_nodes
            for child in (curr.left, curr.right) if child
            ]
    # {inv && cur_depth_nodes is empty ==> result has all nodes}
    return result
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
