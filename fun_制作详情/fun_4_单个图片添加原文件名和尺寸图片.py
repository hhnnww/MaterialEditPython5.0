from PIL import Image

from fun_图片处理 import fun_图片竖向拼接

from .fun_5_图片查找源文件地址 import fun_图片转换成源文件地址
from .fun_6_构建尺寸标题 import fun_构建尺寸标题
from .fun_7_制作文件名和尺寸图 import fun_制作源文件名字和尺寸信息图片
from .type import ImageModel, MakeProductPageModel


def fun_生成源文件名称和格式的图片(
    im: Image.Image,
    image: ImageModel,
    item: MakeProductPageModel,
    ori_size: tuple[int, int],
):
    name_str, size_str = "", "-"
    material_ori_file = fun_图片转换成源文件地址(
        image.path, material_path=item.material_folder
    )
    if material_ori_file is not None:
        name_str = material_ori_file.name
        size_str = fun_构建尺寸标题(path=material_ori_file, ori_size=ori_size)

        info_pil = fun_制作源文件名字和尺寸信息图片(name_str=name_str, size_str=size_str)
        info_pil.thumbnail((int(im.width * 0.9), 9999), resample=Image.LANCZOS)

        im = fun_图片竖向拼接([im, info_pil], 40, "center")

    return im
