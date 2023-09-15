from PIL import Image

from fun_图片处理 import (
    fun_图片居中粘贴,
    fun_图片横向拼接,
    fun_图片添加圆角,
    fun_图片蜘蛛水印,
    fun_图片裁剪,
    fun_画边框,
)

from .fun_4_单个图片添加原文件名和尺寸图片 import fun_生成源文件名称和格式的图片
from .type import ImageModel, MakeXQModel


def fun_制作单行图片(image_list: list[ImageModel], item: MakeXQModel) -> Image.Image:
    col_width = (item.xq_width - ((len(image_list) + 1) * item.spacing)) / sum(
        [k.ratio for k in image_list]
    )

    l = []
    height = 0
    for image in image_list:
        width = int(col_width * image.ratio)
        height = int((col_width * image.ratio) / image.ratio)

        if height > 2000:
            width = int(
                (item.xq_width - ((len(image_list) + 1) * item.spacing))
                / len(image_list)
            )
            height = 2000

        im = fun_制作单个图片(image, width=width, height=height, item=item)
        l.append(im)

    im = fun_图片横向拼接(l, spacing=item.spacing, diection="start")
    im = fun_图片居中粘贴(im, item.xq_width, im.height, (255, 255, 255, 255))

    return im


def fun_制作单个图片(
    image: ImageModel,
    item: MakeXQModel,
    width: int,
    height: int,
) -> Image.Image:
    im = Image.open(image.path).convert("RGBA")
    ori_size = im.size
    im = fun_图片居中粘贴(im, im.width, im.height, (255, 255, 255, 255))

    im = fun_图片裁剪(
        im=im,
        crop_size_width=width,
        crop_size_height=height,
        direction=item.crop_position,
    )
    im = fun_画边框(im=im, border_color=(240, 240, 240, 255))
    im = fun_图片蜘蛛水印(im, 80, 3, 1)
    im = fun_图片添加圆角(im, 15)

    if item.has_info:
        im = fun_生成源文件名称和格式的图片(im=im, image=image, item=item, ori_size=ori_size)

    return im
