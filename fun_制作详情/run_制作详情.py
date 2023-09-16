from typing import Literal

from PIL import Image
from tqdm import tqdm

from fun_图片处理 import fun_图片竖向拼接

from .fun_1_构建所有图片 import fun_构建所有图片
from .fun_1_构建指定图片列表 import fun_构建指定图片
from .fun_2_图片详情分组 import fun_图片详情分组
from .fun_3_制作单行图片 import fun_制作单行图片
from .type import MakeProductPageModel


def run_制作文件夹详情(item: MakeProductPageModel):
    """
    1.如果传入了img_list，直接遍历生成IamgeModel,
      如果没有，则把指定文件夹所有的图片遍历出来
    2.然后根据文件名排序
    3.根据使用的图片，裁剪去多余的图片
    4.所有图片读取尺寸和计算比例
    """

    if len(item.image_list) > 0:
        image_list = fun_构建指定图片(img_list=item.image_list)
    else:
        image_list = fun_构建所有图片(
            path=item.image_dir_path,
            use_iamge=item.image_folder,
            sort=item.image_sort,
        )

    """
    1.根据图片比例进行组合，一行2个还是3个
    2.超出的宽度自动换行
    """
    comb_image_list = fun_图片详情分组(
        image_list=image_list,
        line_num=item.online_image_number,
        line_ratio=item.image_radio_number,
    )

    """
    1.制作横着的单行图图片，并构建成列表，
    2.根据图片列表，来生成完整图片。
    """

    l = []
    for image_list in tqdm(comb_image_list, ncols=100, desc="制作详情\t"):
        l.append(fun_制作单行图片(image_list=image_list, item=item))

    """
    如果没有素材信息的效果图
    间距为80
    """
    line_spacing = 180
    if item.contains_image_information is False:
        line_spacing = 80
    with fun_图片竖向拼接(pil_list=l, spacing=line_spacing, diection="start") as im:
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        bg.paste(im, (0, 0), im)

    return bg
