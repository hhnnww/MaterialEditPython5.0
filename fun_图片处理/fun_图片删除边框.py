from typing import Optional

from PIL import Image, ImageChops


def fun_删除图片边框(
    im: Image.Image, border_color: Optional[tuple[int, int, int, int]] = None
) -> Image.Image:
    """
    如果start_color是None
    获取图片的第一个像素颜色
    如果不是，则根据给出的颜色查找

    然后两个图片寻找差异，如果有差异，就直接裁剪输出

    Args:
        im: 需要删除边框的图片
        border_color: 边框颜色，如果没有指定，就获取图片第一个像素点的颜色作为边框颜色

    Returns:
        Image.Image: 裁剪后的图片
    """
    if border_color is None:
        bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    else:
        bg = Image.new(im.mode, im.size, (255, 255, 255, 0))

    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()

    if bbox:
        return im.crop(bbox)

    return im
