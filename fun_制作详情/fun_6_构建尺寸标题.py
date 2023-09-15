from pathlib import Path


def fun_构建尺寸标题(path: Path, ori_size: tuple[int, int]) -> str:
    size_str = "-"
    if path.suffix.lower() in [".psd", ".psb"]:
        size_str = f"{ori_size[0]} × {ori_size[1]} (PX)"
    elif path.suffix.lower() in [".ai", ".eps"]:
        size_str = f"矢量文件"
    elif path.suffix.lower() in [".pptx", ".ppt"]:
        size_str = f"PPT幻灯片"

    return size_str
