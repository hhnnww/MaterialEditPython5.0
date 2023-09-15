from pathlib import Path
from typing import Optional

from PIL import Image

from setting import IMAGE_SUFFIX

from .fun_获取文件名中的数字 import fun_获取文件名中的数字
from .type import ImageModel


def fun_构建所有图片(
    path: str,
    use_iamge: Optional[int] = None,
    sort: bool = True,
) -> list[ImageModel]:
    l = []
    path_obj = Path(path)

    # 判断传递文件夹是否正确
    if not path_obj.is_dir():
        raise IndexError("必须传入文件夹")

    if not path_obj.exists():
        raise IndexError("文件夹不存在")

    # 构建所有图片
    for in_file in path_obj.rglob("*"):
        if in_file.is_file() and in_file.suffix.lower() in IMAGE_SUFFIX:
            l.append(in_file.as_posix())

    # 图片排序
    l.sort(key=lambda k: fun_获取文件名中的数字(k), reverse=not sort)

    # 如果指定了使用图片的数量，进行截断
    if use_iamge:
        l = l[:use_iamge]

    dst_l = []

    # 开始构建图片列表
    for in_file in l:
        with Image.open(in_file) as im:
            dst_l.append(
                ImageModel(
                    path=in_file,
                    width=im.width,
                    height=im.height,
                    ratio=im.width / im.height,
                )
            )

    return dst_l
