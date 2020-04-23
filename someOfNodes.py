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
node20 = Node(20, node16, node25)
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
    
    
def SumOfParentOfX(head, target, result=0):
    
    if head is not None:    
        if head.right is not None and head.right.val == target:
            result += head.val
        elif head.left is not None and head.left.val == target:
            result += head.val
        
    if head.right is not None:
        result += SumOfParentOfX(head.right, target)
        
    if head.left is not None:
        result += SumOfParentOfX(head.left, target)
    
    return result
    
    
def isLeave(node):
    if node is not None:
        if node.left is None and node.right is None:
            return True
    return False
    
    
def sumOfLeftLeaves(head, result=0):
    
    if head is not None:
        if head.left is not None and isLeave(head.left):
            result += head.left.val
            
    if head.left is not None:
        result += sumOfLeftLeaves(head.left)
    
    if head.right is not None:
        result += sumOfLeftLeaves(head.right) 
        
    return result
       
#print(sum_of_nodes(node15))
#print(SumOfChildOfX(node15, 10))
#print(SumOfParentOfX(node15, 8))
print(sumOfLeftLeaves(node15))
