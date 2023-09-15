from typing import Literal

from pydantic import BaseModel


class PICModel(BaseModel):
    """
    单个图片信息

    Arguments:
        BaseModel {_type_} -- _description_
    """

    path: str
    ratio: float
    width: int
    height: int


class PicOneLineModel(BaseModel):
    """
    一排图片信息

    Arguments:
        BaseModel {_type_} -- _description_
    """

    ratio: float
    pic_list: list[PICModel]


class MakeSTModel(BaseModel):
    """
    传递给运行制作布局函数的参数
    这里直接打包
    可以到处传递
    """

    pic_list: list[str]
    line: int
    spacing: int
    bg_width: int
    bg_height: int
    border_radius: int
    crop_layout: Literal["start", "center", "end"]
