from PIL import Image

from .fun_制作图形.fun_制作圆角矩形 import fun_制作圆角矩形


def fun_图片添加圆角(im: Image.Image, border_radius: int) -> Image.Image:
    """
    给图片添加圆角

    Args:
        im: 需要添加圆角的图片
        border_radius: 圆角角度大小

    Returns:
        Image.Image -- 添加了圆角后的图片
    """
    with im:
        circle = fun_制作圆角矩形(
            im.width, im.height, border_radius, (255, 255, 255, 255)
        )
        circle.paste(im, (0, 0), circle)

    return circle
