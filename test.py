from main import main


def test_main():
    return_from_main = main()
    assert return_from_main == 1
