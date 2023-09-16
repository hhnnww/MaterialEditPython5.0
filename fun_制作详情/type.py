from typing import Literal

from pydantic import BaseModel


class ImageModel(BaseModel):
    path: str
    width: int
    height: int
    ratio: float


class MakeProductPageModel(BaseModel):
    """
    image_dir_path:str 预览图目录或效果图目录
    use_image:int 使用的图片张数
    sort:bool 排序方式
    line_num: 单行的图片数量
    line_ratio: 图片的圆角
    material_path: 素材文件夹
    has_info: bool 是否携带素材信息
    xq_width: int 详情宽度
    spacing: int 图片间距
    crop_position: Literal["start", "center", "end"] 长图的裁剪方式
    img_list: list[str] = [] 使用指定图片制作详情
    """

    image_dir_path: str
    image_folder: int
    image_sort: bool
    online_image_number: int
    image_radio_number: float
    material_folder: str
    contains_image_information: bool
    product_page_width: int
    spacing: int
    crop_position: Literal["start", "center", "end"]
    image_list: list[str] = []
