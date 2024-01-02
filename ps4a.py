# Problem Set 4A
# Name: <Hem N Chaudhary>
# Collaborators:None
# Time Spent: approx 2hr
# Late Days Used: x

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
treeA = [[14,19],[[3,5],0]] # TODO: change this assignment
treeB = [[9,3],6] # TODO: change this assignment
treeC = [[7],[16,4,2],[8]] # TODO: change this assignment


# Part A1: Multiplication on tree leaves

def add_tree(tree):
    """
    Recursively computes the sum of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the sum of all the leaves of the tree.

    """

    # TODO: Your code here
    if len(tree)==0:
        return 0
    elif isinstance(tree[0],int):
        return tree[0]+add_tree(tree[1:])
    
    elif isinstance(tree[0],list):
        return add_tree(tree[0])+add_tree(tree[1:])
        


# Part A2: Arbitrary operations on tree leaves

def sumem(a, b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b


def prod(a, b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b


def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """

    # TODO: Your code here
    if len(tree)==0:
        return base_case
    elif isinstance(tree[0],int):
        return op(tree[0],op_tree(tree[1:],op,base_case))
    
    elif isinstance(tree[0],list):
        return op(op_tree(tree[0],op,base_case),op_tree(tree[1:],op,base_case))


# Part A3: Searching a tree

def search_greater_ten(a, b):
    """
    Operator function that searches for greater-than-10 values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or > 10, and False otherwise
    """

    # TODO: Your code here
    if isinstance(a,bool) and isinstance(b,bool):
        return a or b
    
    elif isinstance(a,bool) or isinstance(b,bool):
        if isinstance(a,bool):
            return a or b>10
        else:
            return a>10 or b
            
    elif isinstance(a,int) or isinstance(b,int):
        return a>10 or b>10
    
        


# Part A4: Find the maximum element of a tree using op_tree and max() in the
# main function below (remembering to pass the function in without parenthesis)
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    a=op_tree([],max,0)
    print(a)
