import re
from pathlib import Path


def fun_获取文件名中的数字(path: str) -> int:
    num_list = re.findall(r"\d+", Path(path).stem)
    if len(num_list) > 0:
        return int("".join(num_list))
    return 0


if __name__ == "__main__":
    n = fun_获取文件名中的数字(r"G:\饭桶设计\2000-2999\2695\2695\饭桶设计12312(1123).png")
    print(n)
