class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right
class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    def build_from(self, cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历我们构造 node 节点
        第二次遍历我们给 root 和 孩子赋值

        :param node_list: [{'data': 'A', 'left': None, 'right': None, 'is_root': False}, ... ...]
        """
        node_dict = {}
        '''
        node_dict = {'A': BinTreeNode('A'), 'B': BinTreeNode('B')}
        '''
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
# 先序遍历
def preorder_tranv(subtree):
    if subtree is not None:
        print(subtree.data)
        preorder_tranv(subtree.left)
        preorder_tranv(subtree.right)
# 中序遍历
def midorder_tranv(subtree):
    if(subtree) is not None:
        midorder_tranv(subtree.left)
        print(subtree.data)
        midorder_tranv(subtree.right)
# 后序遍历
def postorder_tranv(subtree):
    if(subtree) is not None:
        postorder_tranv(subtree.left)
        postorder_tranv(subtree.right)
        print(subtree.data)

# 层序遍历
'''
从根节点开始，打出根，打出左(放入下一次遍历的数组)，打出右(放入下一次遍历的数组)
维护两个数组，一个放正在遍历的节点，一个放下次需要遍历的节点
'''
def layer_tranv(subtree):
    cur_nodes = [subtree]
    next_nodes = []
    while cur_nodes or next_nodes:
        for node in cur_nodes:
            print(node.data)
            if(node.left):
                next_nodes.append(node.left)
            if(node.right):
                next_nodes.append(node.right)
        cur_nodes = next_nodes
        next_nodes = []



# 反转二叉树
def reverse_tree(subtree):
    if subtree is not None:
        subtree.left, subtree.right = subtree.right, subtree.left
        reverse_tree(subtree.left)
        reverse_tree(subtree.right)
