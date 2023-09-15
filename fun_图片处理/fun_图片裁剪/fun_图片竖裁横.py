from typing import Literal

from PIL import Image


def fun_图片竖裁横(
    im: Image.Image,
    crop_size_width: int,
    crop_size_height: int,
    direction: Literal["start", "center", "end"],
) -> Image.Image:
    """
    一个竖图，从中裁剪出横图
    left固定，top则可以上中下移动来寻找合适裁剪位置

    Returns:
        Image.Image -- 裁剪后的图片
    """
    ratio = crop_size_width / crop_size_height
    ori_height = int(im.width / ratio)

    left, top, right, bottom = 0, 0, im.width, 0

    match direction:
        case "start":
            bottom = ori_height
        case "center":
            top = int((im.height - ori_height) / 2)
            bottom = ori_height + top
        case "end":
            top = im.height - ori_height
            bottom = im.height

    return im.resize(
        (crop_size_width, crop_size_height),
        resample=Image.LANCZOS,
        box=(left, top, right, bottom),
        reducing_gap=3,
    )


if __name__ == "__main__":
    im = fun_图片竖裁横(
        Image.open(r"C:\Users\wuweihua\Desktop\UPLOAD\0.jpg"),
        1500,
        500,
        "end",
    )
    print(im.size)
    im.show()
