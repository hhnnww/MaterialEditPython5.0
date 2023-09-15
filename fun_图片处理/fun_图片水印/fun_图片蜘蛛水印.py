from PIL import Image

from ..fun_图片拼接.fun_图片横向拼接 import fun_图片横向拼接
from ..fun_图片拼接.fun_图片竖向拼接 import fun_图片竖向拼接
from .fun_获取单个水印 import fun_获取单个水印


def fun_图片蜘蛛水印(
    im: Image.Image, logo_size: int, line: int, line_num: int
) -> Image.Image:
    """
    给传入的图片打上蜘蛛水印

    Args:
        im: 需要打水印的图片
        logo_size: 设置水印大小
        line: 设置水印行数
        line_num: 设置没一行水印的数量

    Returns:
        Image.Image -- 打满水印的图片
    """
    if im.mode != "RGBA":
        im = im.convert("RGBA")

    logo_row = fun_组合水印排列(line_num=line_num, line=line)

    logo_pil_row = []
    for x in logo_row:
        logo_pil_row.append(fun_获取单排水印(im.width, x, logo_size))

    spacing = int((im.height - (logo_size * (line + 1))) / (line))
    logo_comb_pil = fun_图片竖向拼接(
        pil_list=logo_pil_row, spacing=spacing, diection="center"
    )

    im.paste(
        logo_comb_pil,
        (
            int((im.width - logo_comb_pil.width) / 2),
            int((im.height - logo_comb_pil.height) / 2),
        ),
        logo_comb_pil,
    )
    return im


def fun_组合水印排列(line_num: int, line: int) -> list[int]:
    """
    输入每一行水印数量和行数，来自动进行排列

    Args:
        line_num: 每一行的水印数量，以较小为基数
        line: 需要打多少行水印

    Returns:
        list[int] -- 自动排列后的列表
    """
    ori_list = [line_num, line_num + 1]

    comb_list = []
    for x in range(line - 1):
        comb_list.extend(ori_list)

    return comb_list[:line]


def fun_获取单排水印(width: int, line_num: int, logo_size: int) -> Image.Image:
    """
    自动计算一行水印在图片中排列的间隔
    然后横向拼接水印

    Args:
        width: 图片宽度
        line_num: 一排放多少个水印
        logo_size: 水印宽度

    Returns:
        Image.Image -- 横排单排拼接后的水印
    """
    color = int(255 * 0.5)
    alpha = int(255 * 0.39)
    logo_pil = fun_获取单个水印(logo_size, (color, color, color, alpha))
    spacing = int((width - (line_num * logo_pil.width)) / line_num)

    im = fun_图片横向拼接(
        pil_list=[logo_pil.copy() for x in range(line_num)],
        spacing=spacing,
        diection="start",
    )

    return im
