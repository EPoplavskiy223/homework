import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_log_decorator_success(capsys: CaptureFixture[str]) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result: int = add(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "add ok" in captured.out


def test_log_decorator_error(capsys: CaptureFixture[str]) -> None:
    @log()
    def div(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out
