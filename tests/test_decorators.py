from src.decorators import log


def test_log():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3


def test_log_if_no_arg():
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    assert my_function(1, 2) == "3\nmy_function ok"


def test_log_if_error():
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, [])
    assert my_function(1, []) == ("my_function error: unsupported operand type(s)"
                                  " for +: 'int' and 'list'. Inputs: (1, []), {}")
