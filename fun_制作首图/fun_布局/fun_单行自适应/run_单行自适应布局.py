from typing import Literal

from PIL import Image

from ....fun_图片处理 import fun_图片竖向拼接
from ..fun_构建图片 import fun_构建图片
from ..type import MakeSTModel
from .fun_1_构建所有单行 import fun_1_所有单行
from .fun_2_单行排序 import fun_2_单行排序
from .fun_3_确定结构 import fun_3_确定结构
from .fun_4_制作单行图片 import fun_制作单行图片


def run_单行自适应布局(item_in: MakeSTModel) -> Image.Image:
    pic_model_list = fun_构建图片(pic_path_list=item_in.pic_list)
    comb_list = fun_1_所有单行(pic_list=pic_model_list, line=item_in.line)
    comb_list = fun_2_单行排序(
        line_list=comb_list,
        line=item_in.line,
        bg_width=item_in.bg_width,
        bg_height=item_in.bg_height,
    )
    st_list = fun_3_确定结构(line_list=comb_list, line=item_in.line)

    im_list = []
    for line_list in st_list:
        line_im = fun_制作单行图片(
            pic_list=line_list,
            spacing=item_in.spacing,
            line=item_in.line,
            bg_width=item_in.bg_width,
            bg_height=item_in.bg_height,
            border_radius=item_in.border_radius,
            crop_layout=item_in.crop_layout,
        )
        im_list.append(line_im)

    with fun_图片竖向拼接(
        pil_list=im_list, spacing=item_in.spacing, diection="start"
    ) as im:
        bg = Image.new(
            "RGBA", (item_in.bg_width, item_in.bg_height), (255, 255, 255, 255)
        )
        left = int((bg.width - im.width) / 2)
        top = int((bg.height - im.height) / 2)
        bg.paste(im, (left, top), im)

    return bg
