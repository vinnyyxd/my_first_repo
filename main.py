'''
Docstring for main
'''
import random


def main() -> list[int]:
    """_summary_

    Returns:
        list[int]: _description_
    """
    _list = [random.randint(0, 20) for _ in range(50)]
    return _list
