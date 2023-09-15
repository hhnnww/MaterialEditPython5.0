from typing import Literal

from PIL import Image

from .fun_图片横裁竖 import fun_图片横裁竖
from .fun_图片竖裁横 import fun_图片竖裁横


def fun_图片裁剪(
    im: Image.Image,
    crop_size_width: int,
    crop_size_height: int,
    direction: Literal["start", "center", "end"],
) -> Image.Image:
    """
    根据指定大小裁剪图片
    自动缩放后裁剪

    Returns:
        Image.Image: 图片
    """
    if im.width / im.height > crop_size_width / crop_size_height:
        return fun_图片横裁竖(
            im=im,
            crop_size_height=crop_size_height,
            crop_size_width=crop_size_width,
            direction=direction,
        )

    elif im.width / im.height < crop_size_width / crop_size_height:
        return fun_图片竖裁横(
            im=im,
            crop_size_height=crop_size_height,
            crop_size_width=crop_size_width,
            direction=direction,
        )

    else:
        return im.resize(
            size=(crop_size_width, crop_size_height),
            resample=Image.LANCZOS,
            reducing_gap=3,
        )
