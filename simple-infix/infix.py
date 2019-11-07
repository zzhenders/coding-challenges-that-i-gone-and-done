"""Simple infix calculator.

    >>> calc("1 + 2")
    3

    >>> calc("2 * 3")
    6

    >>> calc("2 * ( 1 + 2 )")
    6

    >>> calc("( 2 * 1 ) + 2")
    4

    >>> calc("( ( 1 + 2 ) * ( 3 + 4 ) ) - ( 2 * ( 1 + 3 ) )")
    13
"""


class Expression(object):
    def __init__(self, parent=None):
        self.operator = None
        self.operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }
        self.left = None
        self.right = None
        self.parent = parent

    def set_operator(self, operator):
        self.operator = self.operators[operator]

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def evaluate(self):
        if not type(self.left) is int:
            self.left = self.left.evaluate()
        if not type(self.right) is int:
            self.right = self.right.evaluate()
        return self.operator(self.left, self.right)


def calc(s):
    """Simple infix calculator."""

    root = Expression()
    current_node = root
    position = ["l"]     # where in the tree we are

    for item in s.split():
        if item == "(":
            # go deeper
            if position[-1] == "l":
                current_node.set_left(Expression(parent=current_node))
                current_node = current_node.left
                position.append("l")
            else:
                current_node.set_right(Expression(parent=current_node))
                current_node = current_node.right
                position.append("l")

        elif item == ")":
            # go back up
            current_node = current_node.parent
            position.pop()
        elif item in "+-/*":
            # item is an operator
            position[-1] = "r"
            current_node.set_operator(item)
        else:
            # item is a number
            if position[-1] == "l":
                current_node.set_left(int(item))
            else:
                current_node.set_right(int(item))

    return root.evaluate()

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n")
