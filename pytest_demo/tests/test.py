# from pytest_demo.src.main import main
import pytest_demo.src.main as main


def test_main():
    return_from_main = main.main()
    assert return_from_main == 1
