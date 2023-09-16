from PIL import Image

from ..fun_图片处理 import (
    fun_单行字体转图片,
    fun_图片居中粘贴,
    fun_图片横向拼接,
    fun_图片添加圆角,
    fun_图片竖向拼接,
    fun_画边框,
    fun_获取字体,
    fun_长本文分行,
)
from .type import OneLineInfoModel


def run_制作数据图(item: list[OneLineInfoModel]) -> Image.Image:
    im = fun_图片竖向拼接(
        [fun_制作单行(obj, num) for num, obj in enumerate(item)],
        spacing=0,
        diection="start",
        background=(255, 255, 255, 255),
    )
    im = fun_图片居中粘贴(im, 1500 - 40, im.height, (255, 255, 255, 255))
    im = fun_画边框(im, border_color=(240, 240, 240, 255))
    im = fun_图片添加圆角(im, 20)
    im = fun_图片居中粘贴(
        im, width=1500, height=im.height + 40, background=(255, 255, 255, 255)
    )
    return im


def fun_制作单行(item: OneLineInfoModel, sort: int) -> Image.Image:
    if sort % 2 != 0:
        bg_color = (249, 249, 249, 255)
    else:
        bg_color = (255, 255, 255, 255)

    font_color = (120, 120, 150, 255)
    size = 40

    title_pil = fun_单行字体转图片(
        text=item.title,
        en_font_path=fun_获取字体("montserrat").normal,
        cn_font_path=fun_获取字体("opposans").normal,
        size=size,
        fill=font_color,
        bg_color=bg_color,
    )

    desc_text_list = fun_长本文分行(item.desc, 25)
    desc_pil = fun_图片竖向拼接(
        [
            fun_单行字体转图片(
                text=text,
                en_font_path=fun_获取字体("montserrat").normal,
                cn_font_path=fun_获取字体("opposans").normal,
                size=size,
                fill=font_color,
                bg_color=bg_color,
            )
            for text in desc_text_list
        ],
        spacing=20,
        diection="start",
        background=bg_color,
    )

    spacing = 100 - title_pil.width + 200
    with fun_图片横向拼接(
        [title_pil, desc_pil], spacing=spacing, diection="start"
    ) as im:
        bg = Image.new("RGBA", (1500, im.height + 140), bg_color)
        bg.paste(im, (100, 70), im)

    return bg
