from PIL import Image, ImageDraw, ImageFont

from ..fun_图片删除边框 import fun_删除图片边框
from .fun_判断会否是英文 import fun_是英文
from .fun_获取字体大小 import fun_获取字体大小


def fun_单行字体转图片(
    text: str,
    en_font_path: str,
    cn_font_path: str,
    fill: tuple[int, int, int, int] = (255, 255, 255, 255),
    bg_color: tuple[int, int, int, int] = (255, 255, 255, 0),
    size: int = 200,
    en_margin_top: float = 0,
    en_ratio: float = 1,
) -> Image.Image:
    """
    单行文字转图片

    Args:
        en_margin_top: 英文往上面提一提
        en_ratio: 英文放大倍率

    Returns:
        _type_: PIL 图片
    """

    # 英文字体扩大倍数和单行向上提升倍数
    en_size_ratio = int(size * en_ratio)
    en_top_padding = 0 - int(size * en_margin_top)

    en_font_true = ImageFont.truetype(font=en_font_path, size=en_size_ratio)
    cn_font_true = ImageFont.truetype(font=cn_font_path, size=size)

    # 计算背景图片大小
    width, height = 0, 0
    for letter in text:
        if fun_是英文(letter=letter):
            font_size = fun_获取字体大小(letter=letter, font_true=en_font_true)
        else:
            font_size = fun_获取字体大小(letter=letter, font_true=cn_font_true)

        width += font_size.width
        if font_size.height > height:
            height = font_size.height

    # 开始制作图片
    bg = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(bg)

    left = 0
    for letter in text:
        if fun_是英文(letter=letter):
            draw.text(
                xy=(left, en_top_padding),
                text=letter,
                fill=fill,
                font=en_font_true,
            )
            left += fun_获取字体大小(letter=letter, font_true=en_font_true).width
        else:
            draw.text(xy=(left, 0), text=letter, fill=fill, font=cn_font_true)
            left += fun_获取字体大小(letter=letter, font_true=cn_font_true).width

    bg = fun_删除图片边框(bg)

    return bg
