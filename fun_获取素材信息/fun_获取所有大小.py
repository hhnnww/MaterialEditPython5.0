from pathlib import Path


def fun_获取所有大小(all_file: list[Path]):
    all_size = sum([in_file.stat().st_size for in_file in all_file])

    size_name_list = ["bytes", "kb", "mb", "gb"]

    num = 0
    while all_size > 1024:
        all_size = all_size / 1024
        num += 1

    return f"{round(all_size,2)} {size_name_list[num].upper()}"
