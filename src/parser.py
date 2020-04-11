from typing import Set

from jinja2 import Environment, meta

PARSER_HANDLER: Environment = Environment()


def render_template(source: str, *args, **kwargs) -> str:
    """
    Render a Jinaja templates string with variables

    :param source: A Jinja Template presented as a string
    :type source: str
    :return: Rendered template as unicode string
    :rtype: str
    """
    template = PARSER_HANDLER.from_string(source)
    return template.render(*args, **kwargs)


def parse_template_variables(source: str, name=None, filename=None) -> Set[str]:
    """
    Parse a Jinja template string and return a set of undeclared variables

    :param source: A Jinja Template presented as a string
    :type source: str
    :return: A set of undeclared variables in the template
    :rtype: Set[str]
    """
    ast = _parse_template(source, name, filename)
    return _find_undeclared_variables(ast)


def _parse_template(source: str, name=None, filename=None):
    """Parse a Jinja template and return the Abstract Syntax Tree (AST)"""
    ast = PARSER_HANDLER.parse(source)
    return ast


def _find_undeclared_variables(ast) -> Set[str]:
    """Find all undeclared variables in a Jinja Abstract Syntax Tree (AST)"""
    return meta.find_undeclared_variables(ast)
