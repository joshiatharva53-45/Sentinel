"""
Calculator Plugin
"""

import ast
import operator as op


def initialize():
    print("Calculator Plugin Initialized")


# Supported operators
_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def _evaluate(node):

    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.Num):  # Python <3.8 compatibility
        return node.n

    if isinstance(node, ast.BinOp):
        return _OPERATORS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right),
        )

    if isinstance(node, ast.UnaryOp):
        return _OPERATORS[type(node.op)](
            _evaluate(node.operand),
        )

    raise TypeError(node)


def safe_eval(expression: str):

    tree = ast.parse(expression, mode="eval")

    return _evaluate(tree.body)


def execute(command: str):

    command = command.lower().strip()

    prefixes = (
        "calculate",
        "calc",
        "what is",
        "evaluate",
    )

    expression = command

    for prefix in prefixes:

        if expression.startswith(prefix):
            expression = expression[len(prefix):].strip()

    if not expression:
        return "Nothing to calculate."

    try:

        result = safe_eval(expression)

        return f"{expression} = {result}"

    except Exception:

        return None