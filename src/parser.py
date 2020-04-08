from jinja2 import Environment, meta


PARSER_HANDLE = Environment()


def parse_template_variables(source, name=None, filename=None):
    ast = _parse_template(source, name, filename)
    return _find_undeclared_variables(ast)


def _parse_template(source, name=None, filename=None):
    """Parse a Jinja template and return the Abstract Syntax Tree (AST)"""
    ast = PARSER_HANDLE.parse(source)
    return ast 


def _find_undeclared_variables(ast) -> set:
    """"""
    return meta.find_undeclared_variables(ast)