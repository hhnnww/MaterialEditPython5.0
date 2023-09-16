from fastapi import APIRouter
from pydantic import BaseModel

from fun_获取素材信息.fun_构建文件夹 import PathModel, fun_构建文件夹
from fun_获取素材信息.run_获取所有图片 import ImageModel, run_获取所有图片
from fun_获取素材信息.run_获取素材信息 import MaterialInfoModel, run_获取素材信息

router = APIRouter(prefix="/GetMaterialInfo")


class Item(BaseModel):
    rootPath: str
    tbName: str


class Res(PathModel, MaterialInfoModel):
    preview_image_list: list[ImageModel]
    preview_image_count: int

    effect_image_list: list[ImageModel]
    effect_image_count: int


@router.post("", response_model=Res)
def get_material_info(item: Item):
    path_model = fun_构建文件夹(root_path=item.rootPath)
    ma_info_model = run_获取素材信息(material_path=path_model.material_path)

    res_dict = dict()
    res_dict.update(path_model.model_dump())
    res_dict.update(ma_info_model.model_dump())

    pre_list = run_获取所有图片(path_model.preview_image_path)
    res_dict.update(
        {"preview_image_list": pre_list, "preview_image_count": len(pre_list)}
    )

    eff_list = run_获取所有图片(path_model.effect_image_path)
    res_dict.update(
        {"effect_image_list": eff_list, "effect_image_count": len(eff_list)}
    )

    return res_dict
