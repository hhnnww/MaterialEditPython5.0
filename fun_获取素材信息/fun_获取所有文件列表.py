from pathlib import Path


def fun_获取所有文件列表(ma_path_obj: Path) -> list[Path]:
    all_file = []
    for in_file in ma_path_obj.rglob("*"):
        if in_file.is_file():
            all_file.append(in_file)

    return all_file
