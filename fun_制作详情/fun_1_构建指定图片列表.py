from PIL import Image

from .type import ImageModel


def fun_构建指定图片(img_list: list[str]) -> list[ImageModel]:
    dst_l = []

    # 开始构建图片列表
    for in_file in img_list:
        with Image.open(in_file) as im:
            dst_l.append(
                ImageModel(
                    path=in_file,
                    width=im.width,
                    height=im.height,
                    ratio=im.width / im.height,
                )
            )

    return dst_l
