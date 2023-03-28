import sys
from antlr4 import *
from stella.stellaParser import stellaParser
from stella.stellaLexer import stellaLexer


def handle_expr_context(ctx: stellaParser.ExprContext):
    if isinstance(ctx, stellaParser.ConstTrueContext):
        pass
    elif isinstance(ctx, stellaParser.ConstFalseContext):
        pass
    elif isinstance(ctx, stellaParser.IfContext):
        # ctx.condition
        # ctx.thenExpr
        # ctx.elseExpr
        pass
    elif isinstance(ctx, stellaParser.VarContext):
        print("I have seen a variable:", ctx.name.text)
    else:
        pass # raise RuntimeError("unsupported syntax")


def handle_decl_context(ctx: stellaParser.DeclContext):
    if isinstance(ctx, stellaParser.DeclFunContext):
        print("Declaring function", ctx.name.text)
        # ctx.paramDecls
        # ctx.returnType
        handle_expr_context(ctx.returnExpr)
    elif isinstance(ctx, stellaParser.DeclTypeAliasContext):
        raise RuntimeError("unsupported syntax")
    else:
        raise RuntimeError("unsupported syntax")


def handle_program_context(ctx: stellaParser.ProgramContext):
    for decl in ctx.decls:
        handle_decl_context(decl)


def main(argv):
    if len(argv) > 1:
        input_stream = FileStream(argv[1])
    else:
        input_stream = StdinStream()
    lexer = stellaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = stellaParser(stream)

    program = parser.program()
    handle_program_context(program)


if __name__ == '__main__':
    main(sys.argv)
