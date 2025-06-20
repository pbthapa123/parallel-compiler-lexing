# Class representing a node in the Abstract Syntax Tree (AST)
class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value      # Node value (operator or operand)
        self.left = left        # Left child node
        self.right = right      # Right child node

    def __repr__(self):
        # Representation for printing/debugging the AST structure
        return f"ASTNode({self.value}, {self.left}, {self.right})"

# Parser class for converting tokens into an Abstract Syntax Tree (AST)
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens                        # Input list of tokens
        self.current_token_index = 0                # Index of the current token being parsed

    def current_token(self):
        # Return the current token if within bounds
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None  # Return None if no more tokens

    def advance(self):
        # Move to the next token
        if self.current_token_index < len(self.tokens):
            self.current_token_index += 1

    def parse_expression(self):
        # Parse addition and subtraction expressions
        left = self.parse_term()  # Parse the left side of the expression
        while self.current_token() in ('+', '-'):
            operator = self.current_token()  # Store the operator
            self.advance()                   # Move past the operator
            right = self.parse_term()        # Parse the right side
            left = ASTNode(operator, left, right)  # Combine into a new AST node
        return left

    def parse_term(self):
        # Parse multiplication and division expressions
        left = self.parse_factor()  # Parse the left side of the term
        while self.current_token() in ('*', '/'):
            operator = self.current_token()  # Store the operator
            self.advance()                   # Move past the operator
            right = self.parse_factor()      # Parse the right side
            left = ASTNode(operator, left, right)  # Combine into a new AST node
        return left

    def parse_factor(self):
        token = self.current_token()  # Get the current token

        if token.isdigit(): 
            self.advance()
            return ASTNode(token)  # Create a leaf node with the number

        elif token.isalpha():  
            self.advance()
            return ASTNode(token)  # Create a leaf node with the identifier

        elif token == '(': 
            self.advance()               # Move past '('
            expr = self.parse_expression()  # Recursively parse the inner expression
            if self.current_token() == ')':
                self.advance()           # Move past ')'
            return expr                  # Return the parsed subexpression

        else:
            # Raise an error for unexpected token
            raise SyntaxError(f"Unexpected token {token}")

    def parse(self):
        # Entry point for parsing
        return self.parse_expression()

# Example Usage:
tokens = ['x', '=', '5', '+', '3', '*', '2']  # Tokenized input
parser = Parser(tokens)
ast = parser.parse()                          # Parse tokens into an AST
print(ast)                                     # Output the AST
