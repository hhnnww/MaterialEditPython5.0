from typing import Literal

from PIL import Image

from ....fun_图片处理 import fun_图片横向拼接, fun_图片添加圆角, fun_图片竖向拼接, fun_图片裁剪
from ..type import PICModel


def fun_制作首图(
    pic_list: list[PICModel],
    bg_width: int,
    bg_height: int,
    line: int,
    line_col: int,
    spacing: int,
    direction: Literal["start", "center", "end"],
    border_radius: int,
) -> Image.Image:
    small_im_width = int((bg_width - ((line_col + 1) * spacing)) / line_col)
    small_im_height = int((bg_height - ((line + 1) * spacing)) / line)

    comb_list = [
        pic_list[i : i + line_col] for i in range(0, len(pic_list), line_col)
    ]

    all_comb_list = []
    for line_comb in comb_list:
        one_line_list = []
        for one_pic in line_comb:
            im = fun_制作单个图片(
                pic=one_pic,
                width=small_im_width,
                height=small_im_height,
                spacing=spacing,
                direction=direction,
                border_radius=border_radius,
            )
            one_line_list.append(im)

        one_line_pil = fun_图片横向拼接(
            pil_list=one_line_list, spacing=spacing, diection="center"
        )
        all_comb_list.append(one_line_pil)

    with fun_图片竖向拼接(
        pil_list=all_comb_list, spacing=spacing, diection="center"
    ) as bg:
        new_bg = Image.new("RGBA", (bg_width, bg_height), (255, 255, 255, 255))
        new_bg.paste(
            bg,
            (
                int((new_bg.width - bg.width) / 2),
                int((new_bg.height - bg.height) / 2),
            ),
            bg,
        )

    return new_bg


def fun_制作单个图片(
    pic: PICModel,
    width: int,
    height: int,
    spacing: int,
    direction: Literal["start", "center", "end"],
    border_radius: int,
):
    im = Image.open(pic.path)
    im = fun_图片裁剪(
        im=im,
        crop_size_width=width,
        crop_size_height=height,
        direction=direction,
    )

    if spacing > 0:
        im = fun_图片添加圆角(im=im, border_radius=border_radius)

    return im
