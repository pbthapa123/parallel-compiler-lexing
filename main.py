from lexer import Lexer  
from parser import Parser
from ir_generator import IRGenerator
from optimizer import Optimizer
from codegen import CodeGenerator

def main():
    # Lexical analysis (not implemented here, assume you have tokens)
    tokens = ['3', '+', '5', '*', '(', '10', '-', '2', ')']

    # Parsing
    parser = Parser(tokens)
    ast = parser.parse()

    # IR Generation
    ir_generator = IRGenerator()
    ir_generator.generate_ir(ast)
    ir = ir_generator.get_ir()

    # Optimization
    optimizer = Optimizer(ir)
    optimized_ir = optimizer.optimize()

    # Code Generation
    code_generator = CodeGenerator(optimized_ir)
    assembly_code = code_generator.generate_code()

    # Print the generated assembly code
    print("\n".join(assembly_code))

if __name__ == "__main__":
    main()
