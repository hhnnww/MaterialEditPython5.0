from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .fun_获取所有大小 import fun_获取所有大小
from .fun_获取所有文件列表 import fun_获取所有文件列表
from .fun_获取源文件列表 import fun_获取源文件列表


class MaterialInfoModel(BaseModel):
    material_size: str
    material_suffix: str

    material_count: int
    material_count_title: str

    material_format_title: str


def run_获取素材信息(material_path: str):
    ma_path_obj = Path(material_path)
    all_file = fun_获取所有文件列表(ma_path_obj)
    dir_size = fun_获取所有大小(all_file=all_file)
    ma_list = fun_获取源文件列表(all_file=all_file)

    ma_dict_title = dict(
        psd="PSD 分层设计素材",
        ai="AI 矢量设计素材",
        eps="EPS 矢量设计市场",
        ppt="PPT 幻灯片素材",
        pptx="PPTX 幻灯片素材",
        otf="otf 字体文件",
        ttf="ttf 字体文件",
    )

    ma_title = ma_dict_title.get(ma_list[0][1].lower())
    if ma_title is None:
        ma_title = ""

    return MaterialInfoModel(
        material_size=dir_size,
        material_suffix=",".join([obj[1] for obj in ma_list]),
        material_count_title=",".join(
            [f"{obj[0]}个 {obj[1]} 文件" for obj in ma_list]
        ),
        material_format_title=ma_title,
        material_count=ma_list[0][0],
    )
