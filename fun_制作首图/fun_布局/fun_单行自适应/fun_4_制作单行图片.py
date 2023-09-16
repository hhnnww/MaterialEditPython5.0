from typing import Literal

from PIL import Image

from ....fun_图片处理 import fun_图片横向拼接, fun_图片添加圆角, fun_图片裁剪
from ..type import PicOneLineModel


def fun_制作单行图片(
    pic_list: PicOneLineModel,
    spacing: int,
    line: int,
    bg_width: int,
    bg_height: int,
    border_radius: int,
    crop_layout: Literal["start", "center", "end"],
) -> Image.Image:
    width = int(bg_width - (spacing * 2))
    height = int((bg_height - ((line + 1) * spacing)) / line)

    ori_width = int(width - ((len(pic_list.pic_list) - 1) * spacing))

    im_list = []
    for pic in pic_list.pic_list:
        im = Image.open(pic.path).convert("RGBA")

        # 计算小图宽度和高度
        # 单行图片高度是固定的，只需要计算单个图片比例，占整行比例的多少。
        # 根据整行宽度，就可以计算单个图片的宽度
        small_im_width = int(ori_width * (pic.ratio / pic_list.ratio)) + 1
        small_im_height = height + 1

        im = fun_图片裁剪(
            im=im,
            crop_size_width=small_im_width,
            crop_size_height=small_im_height,
            direction=crop_layout,
        )

        # 如果有间距，就给图片增加圆角
        if spacing > 0:
            im = fun_图片添加圆角(im, border_radius)

        im_list.append(im)

    return fun_图片横向拼接(pil_list=im_list, spacing=spacing, diection="start")
