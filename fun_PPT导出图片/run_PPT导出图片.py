from pathlib import Path

from .fun_导出操作 import fun_导出操作


def run_PPT导出图片(ppt_path: str):
    img_path = fun_导出操作(ppt_file=ppt_path)


if __name__ == "__main__":
    run_PPT导出图片(r"W:\H000-H999\H0696\H0696\dark.pptx")
