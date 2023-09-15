from pathlib import Path
from typing import Union

from PIL import Image, ImageDraw


def fun_制作圆形(
    diameter: int,
    fill: tuple[int, int, int, int],
    bg_color: tuple[int, int, int, int] = (255, 255, 255, 0),
    ratio: int = 3,
) -> Image.Image:
    """
    画一个圆形

    Returns:
        Image.Image -- 画好圆形的图片
    """
    bg = Image.new("RGBA", (diameter * ratio, diameter * ratio), bg_color)
    draw = ImageDraw.Draw(bg)
    draw.ellipse((0, 0, diameter * ratio, diameter * ratio), fill=fill)
    bg.thumbnail((diameter, diameter), resample=Image.LANCZOS)
    return bg


if __name__ == "__main__":
    fun_制作圆形(200, (255, 255, 255, 255)).show()
