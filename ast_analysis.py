from parser import ASTNode  # Importing the ASTNode class from the parser module

# Recursive function to calculate the depth of an Abstract Syntax Tree (AST)
def calculate_ast_depth(node):
    if node is None:
        return 0  # Base case: if the node is None, depth is 0
    
    # Recursive case: depth is 1 (for the current node) + maximum depth of left or right subtrees
    return 1 + max(calculate_ast_depth(node.left), calculate_ast_depth(node.right))

# Example AST:
ast = ASTNode('+', ASTNode('3'), ASTNode('*', ASTNode('5'), ASTNode('10')))
print("AST Depth:", calculate_ast_depth(ast))
