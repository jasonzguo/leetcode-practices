"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,None,None,3,5]

示例 1:
输入: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。

示例 2:
输入: root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
 

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉搜索树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from lib.treeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = None

        if root is None:
            return result

        nodes = [root]

        dp = {}
        dp[root.val] = None

        while len(nodes) > 0:
            node = nodes.pop(0)

            if node.left is not None:
                dp[node.left.val] = node
                nodes.append(node.left)
            if node.right is not None:
                dp[node.right.val] = node
                nodes.append(node.right)

            if dp[p.val] in dp and dp[q.val] in dp:
                break

        while result is None:
            p_parent = dp[p.val]
            q_parent = dp[q.val]

            if p_parent == q_parent:
                result = dp[p.val]
            elif p_parent == q or p_parent == q.left or p_parent == q.right:
                result = q
            elif q_parent == p or q_parent == p.left or q_parent == p.right:
                result = p
            else:
                if p_parent is not None:
                    p = p_parent
                if q_parent is not None:
                    q = q_parent
        return result


root_a = TreeNode(None)
root_a.direct_insert_multi([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

solution = Solution()
solution.lowestCommonAncestor(root_a, 2, 8).val.should.equal(6)
solution.lowestCommonAncestor(root_a, 2, 4).val.should.equal(2)
solution.lowestCommonAncestor(root_a, 5, 0).val.should.equal(2)
solution.lowestCommonAncestor(root_a, 5, 9).val.should.equal(6)
solution.lowestCommonAncestor(root_a, 2, 5).val.should.equal(2)
