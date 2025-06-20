import time
from lexer import Lexer   # Importing a custom Lexer class to perform lexical analysis

# Function to perform sequential tokenization of the entire input
def sequential_tokenize(input_code):
    lexer = Lexer(input_code)    # Create a single lexer instance for the entire input
    start = time.time()
    lexer.tokenize()
    end = time.time()
    return end - start   # Return the elapsed time

# Function to simulate parallel tokenization by processing each line separately
def mock_parallel_tokenize(input_code):
    lines = input_code.strip().split('\n')
    start = time.time()
    for line in lines:
        lexer = Lexer(line)  # Create a separate lexer for each line.
        lexer.tokenize()
    end = time.time()
    return end - start      # Return the elapsed time

# Example usage:
source_code = "x = 3 + 5 * (10 - 2)\ny = x * 4"
print("Sequential Time:", sequential_tokenize(source_code))
print("Mock Parallel Time:", mock_parallel_tokenize(source_code))
