class Optimizer:
    def __init__(self, ir):
        self.ir = ir

    def constant_folding(self):
        optimized_ir = []
        for instruction in self.ir:
            # If it's a LOAD instruction, we simply add it to the optimized IR
            if 'LOAD' in instruction:
                optimized_ir.append(instruction)
            # Check for ADD and MUL operations to perform constant folding
            elif 'ADD' in instruction or 'MUL' in instruction:
                parts = instruction.split()

                # Ensure that the instruction has the expected format: "OPERATION operand1 operand2"
                if len(parts) == 3:
                    try:
                        # Convert operands to integers and perform constant folding if both are constants
                        left = int(parts[1])
                        right = int(parts[2])

                        if isinstance(left, int) and isinstance(right, int):
                            result = left + right if 'ADD' in instruction else left * right
                            optimized_ir.append(f"LOAD {result}")
                        else:
                            # If not constants, leave the instruction as-is
                            optimized_ir.append(instruction)
                    except ValueError:
                        # If operands are not integers, leave the instruction as-is
                        optimized_ir.append(instruction)
                else:
                    # If the instruction is malformed, leave it as-is
                    optimized_ir.append(instruction)
            else:
                # For any other instructions, just add them as-is
                optimized_ir.append(instruction)
        return optimized_ir

    def optimize(self):
        return self.constant_folding()

# Example Usage:
ir = ['LOAD 3', 'ADD 3 5', 'LOAD 10', 'MUL 5 10']
optimizer = Optimizer(ir)
optimized_ir = optimizer.optimize()
print(optimized_ir)
