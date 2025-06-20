# Class to generate assembly code from intermediate representation (IR)
class CodeGenerator:
    def __init__(self, ir):
        
        self.ir = ir     # Store the intermediate representation (IR) instructions

    def generate_code(self):
        # List to hold generated assembly instructions
        assembly_code = []

        # Iterate through each IR instruction
        for instruction in self.ir:
           
            if 'LOAD' in instruction:
                # Extract the value and generate a LOAD instruction in assembly
                assembly_code.append(f"LOAD R0, {instruction.split()[1]}")
            
            elif 'ADD' in instruction:
                # Generate a generic ADD instruction using placeholder registers
                assembly_code.append("ADD R0, R1, R2")
           
            elif 'MUL' in instruction:
                # Generate a generic MUL instruction using placeholder registers
                assembly_code.append("MUL R0, R1, R2")

        # Return the list of generated assembly instructions
        return assembly_code

# Example usage:
# Define a list of IR instructions
ir = ['LOAD 3', 'ADD 3 5', 'LOAD 10', 'MUL 5 10']

# Create an instance of the CodeGenerator with the IR
code_gen = CodeGenerator(ir)

# Generate assembly code from the IR
assembly_code = code_gen.generate_code()

# Print the resulting assembly instructions, each on a new line
print("\n".join(assembly_code))
