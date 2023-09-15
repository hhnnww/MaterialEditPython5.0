from PIL import Image

from ..fun_构建图片 import fun_构建图片
from ..type import MakeSTModel
from .fun_制作图片 import fun_制作首图
from .fun_计算各种布局的小图比例 import fun_构建所有布局小图比例列表


def run_固定尺寸布局(item_in: MakeSTModel) -> Image.Image:
    pic_list = fun_构建图片(pic_path_list=item_in.pic_list)

    # 计算所有图片的平均比例
    average_ratio = sum([float(p.ratio) for p in pic_list]) / len(pic_list)

    # 构建所有组合的比例列表
    ratio_list = fun_构建所有布局小图比例列表(
        line=item_in.line,
        bg_width=item_in.bg_width,
        bg_height=item_in.bg_height,
    )

    # 查找出最合适的比例
    # 先进行排序，然后选择第一个
    ratio_list.sort(key=lambda k: abs(average_ratio - k.ratio), reverse=False)
    best_layout = ratio_list[0]

    # 图片列表重新排序
    # 并且根据已经计算出来了的单排图片数量
    # 直接传递需要的图片不需要的就不传递了
    pic_list.sort(key=lambda k: abs(best_layout.ratio - k.ratio), reverse=False)
    pic_list = pic_list[: best_layout.line_col * item_in.line]

    return fun_制作首图(
        pic_list=pic_list,
        bg_width=item_in.bg_width,
        bg_height=item_in.bg_height,
        line=item_in.line,
        line_col=best_layout.line_col,
        spacing=item_in.spacing,
        direction=item_in.crop_layout,
        border_radius=item_in.border_radius,
    )
