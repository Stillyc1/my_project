from src.decorators import log


def test_log():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3


def test_log_if_no_arg(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "3\nmy_function ok.\n" in captured.out
