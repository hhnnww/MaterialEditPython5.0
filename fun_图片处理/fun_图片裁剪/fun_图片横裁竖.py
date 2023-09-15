from typing import Literal

from PIL import Image


def fun_图片横裁竖(
    im: Image.Image,
    crop_size_width: int,
    crop_size_height: int,
    direction: Literal["start", "center", "end"],
) -> Image.Image:
    """
    一个横着的图片，从中裁剪出竖着的图
    top固定，left可以左右移动

    Returns:
        Image.Image -- 裁剪后的图片
    """
    ratio = crop_size_width / crop_size_height
    ori_width = int(im.height * ratio)

    left, top, right, bottom = 0, 0, 0, im.height
    match direction:
        case "start":
            left = 0
            right = ori_width
        case "center":
            left = int((im.width - ori_width) / 2)
            right = ori_width + left
        case "end":
            left = im.width - ori_width
            right = im.width

    return im.resize(
        (crop_size_width, crop_size_height),
        resample=Image.LANCZOS,
        box=(left, top, right, bottom),
        reducing_gap=3,
    )


if __name__ == "__main__":
    im = fun_图片横裁竖(
        im=Image.open(r"C:\Users\wuweihua\Desktop\UPLOAD\0.jpg"),
        crop_size_width=300,
        crop_size_height=1500,
        direction="end",
    )
    print(im.size)
    im.show()
