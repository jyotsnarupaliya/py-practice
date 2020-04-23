class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node8 = Node(8)
node12 = Node(12)
node16 = Node(16)
node25 = Node(25)
node10 = Node(10, node8, node12)
node20 = Node(10, node16, node25)
node15 = Node(15, node10, node20)

def sum_of_nodes(head, result=0):
    
    if head is not None:
        result += head.val
        
    if head.right is not None:
        result += sum_of_nodes(head.right)
        
    if head.left is not None:
        result += sum_of_nodes(head.left)
    
    return result
    
def SumOfChildOfX(head, target, result=0):
    
    if head is not None and head.val==target:
        if head.right is not None:
            result += head.right.val
            
        if head.left is not None:
            result += head.left.val
        
    if head.right is not None:
        result += SumOfChildOfX(head.right, target)
        
    if head.left is not None:
        result += SumOfChildOfX(head.left, target)
    
    return result
        
#print(sum_of_nodes(node15))
print(SumOfChildOfX(node15, 10))
