import string


def fun_是英文(letter: str) -> bool:
    """
    判断一个字符是否是英文

    Raises:
        IndexError: 一次只能传递一个字符，传递过长就报错

    Returns:
        bool: 是否是英文
    """
    if len(letter) > 1:
        raise IndexError("传入的本文只能是单个字符：", letter)
    return letter in string.ascii_letters + string.digits


if __name__ == "__main__":
    print(string.ascii_letters)
