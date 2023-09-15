from pathlib import Path

from PIL import Image

from .type import PICModel


def fun_构建图片(pic_path_list: list[str]) -> list[PICModel]:
    if len(pic_path_list) >= 40:
        raise IndexError("制作首图的图片，不能超过或者等于40张")

    p_l = []
    for pic in pic_path_list:
        with Image.open(pic) as im:
            p_l.append(
                PICModel(
                    path=pic,
                    width=im.width,
                    height=im.height,
                    ratio=im.width / im.height,
                )
            )
    return p_l


if __name__ == "__main__":
    from pprint import pprint

    ylt_path = Path(r"F:\小夕素材\10000-10999\10086\预览图")
    p_list = [p.as_posix() for p in ylt_path.iterdir()]
    pprint(list(fun_构建图片(p_list)))
