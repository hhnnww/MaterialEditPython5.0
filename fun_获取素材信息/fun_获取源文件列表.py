from pathlib import Path

from setting import MATERIAL_SUFFIX


def fun_获取源文件列表(all_file: list[Path]) -> list[tuple[int, str]]:
    file_count_list = []
    for suffix in MATERIAL_SUFFIX:
        file_count = len(
            [
                in_file
                for in_file in all_file
                if in_file.suffix.lower() == suffix
            ]
        )
        file_suffix = suffix.upper().replace(".", "")

        if file_count > 0:
            file_count_list.append((file_count, file_suffix))
    file_count_list.sort(key=lambda k: k[0], reverse=True)

    return file_count_list
