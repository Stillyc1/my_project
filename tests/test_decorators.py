from src.decorators import log


def test_log():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3
