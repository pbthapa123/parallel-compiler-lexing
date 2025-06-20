
# A register allocator class that assigns values to a limited set of registers
class RegisterAllocator:
    def __init__(self):
        self.registers = ['R0', 'R1', 'R2', 'R3']
        self.usage = []

    # Allocating a register for the given value
    def allocate(self, val):
        reg = self.registers[len(self.usage) % len(self.registers)]
        self.usage.append((reg, val))   # Record the allocation
        return reg                     # Return the allocated register name

# Example usage:
reg_alloc = RegisterAllocator()
print("Allocated:", reg_alloc.allocate("5"))
print("Allocated:", reg_alloc.allocate("10"))
