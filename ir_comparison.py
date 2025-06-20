# Function to compare the number of IR (Intermediate Representation) instructions
# before and after applying an optimization pass

def instruction_stats(ir_before, ir_after):
    print(f"Instructions Before Optimization: {len(ir_before)}")
    print(f"Instructions After Optimization: {len(ir_after)}")
    print(f"Reduction: {len(ir_before) - len(ir_after)} instructions")

# Example usage:
ir_before = ['LOAD 3', 'LOAD 5', 'LOAD 10', 'MUL', 'ADD']
ir_after = ['LOAD 3', 'LOAD 8', 'LOAD 10', 'LOAD 50']
instruction_stats(ir_before, ir_after)   # Calling the function to display stats
