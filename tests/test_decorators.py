from src.decorators import log


def test_log():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    assert my_function(5, 3) == 8
