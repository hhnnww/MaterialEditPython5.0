from PIL.ImageFont import FreeTypeFont
from pydantic import BaseModel


class SizeModel(BaseModel):
    width: int
    height: int


def fun_获取字体大小(letter: str, font_true: FreeTypeFont) -> SizeModel:
    """
    计算本文转换成图片后，需要的图片大小

    Returns:
        SizeModel: 图片尺寸
    """
    l, t, r, b = font_true.getbbox(letter)
    return SizeModel(width=r, height=b)
