from jinja2 import Environment, meta


PARSER_HANDLE = Environment()


def parse_template(source, name=None, filename=None):
    """Parse a Jinja template and return the Abstract Syntax Tree (AST)"""
    ast = PARSER_HANDLE.parse(source)
    return ast 


def find_undeclared_variables(ast) -> set:
    return meta.find_undeclared_variables(ast)