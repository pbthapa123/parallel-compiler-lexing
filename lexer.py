import re  # Import the regular expressions module for pattern matching


class Lexer:
    def __init__(self, source_code):
        # Store the input source code as a string
        self.source_code = source_code
        
        # Initialize an empty list to store the resulting tokens
        self.tokens = []

    def tokenize(self):
        # Define token patterns as (NAME, REGEX) pairs
        token_specification = [
            ('NUMBER', r'\d+'),          # Integer numbers
            ('ASSIGN', r'='),            # Assignment operator (=)
            ('ID', r'[A-Za-z]+'),        # Identifiers (e.g., variable names)
            ('ADD', r'\+'),              # Addition operator (+)
            ('MUL', r'\*'),              # Multiplication operator (*)
            ('SUB', r'-'),               # Subtraction operator (-)
            ('DIV', r'/'),               # Division operator (/)
            ('LPAREN', r'\('),           # Left parenthesis
            ('RPAREN', r'\)'),           # Right parenthesis
            ('SKIP', r'[ \t\n]+'),       # Skip spaces, tabs, and newlines
            ('MISMATCH', r'.'),          # Any unrecognized character
        ]

        # Combine all token regexes into a single pattern with named groups
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

        # Initialize line number and start position (for potential error reporting)
        line_num = 1
        line_start = 0

        # Iterate over all matches of the token patterns in the source code
        for mo in re.finditer(tok_regex, self.source_code):
            kind = mo.lastgroup       # Token type (e.g., NUMBER, ID, etc.)
            value = mo.group()        # Actual string matched

            # Ignore whitespace and newline characters
            if kind == 'SKIP':
                continue
            # Raise an error for any unexpected characters
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected on line {line_num}')
            else:
                # Append the valid token value to the list
                self.tokens.append(value)

        # Return the list of token values
        return self.tokens
