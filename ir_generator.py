from parser import ASTNode  # Importing ASTNode from parser.py

class IRGenerator:
    def __init__(self):
        self.ir = []  # Holds the generated IR code

    def generate_ir(self, ast):
        # Base case: If the AST node is None, return
        if ast is None:
            return

        # If the current node is a number (digit), load it into the IR
        if ast.value.isdigit():
            self.ir.append(f"LOAD {ast.value}")
        else:
            # Recursively generate IR for the left and right children
            self.generate_ir(ast.left)
            self.generate_ir(ast.right)

            # Process operators (addition, subtraction, multiplication, division)
            if ast.value == '+':
                self.ir.append("ADD")
            elif ast.value == '-':
                self.ir.append("SUB")
            elif ast.value == '*':
                self.ir.append("MUL")
            elif ast.value == '/':
                self.ir.append("DIV")

    def get_ir(self):
        return self.ir

# Example Usage:
# Construct the AST
ast = ASTNode('+', ASTNode('3'), ASTNode('*', ASTNode('5'), ASTNode('10')))

# Create an IRGenerator instance and generate the IR
ir_gen = IRGenerator()
ir_gen.generate_ir(ast)

# Print the generated IR
print(ir_gen.get_ir())
