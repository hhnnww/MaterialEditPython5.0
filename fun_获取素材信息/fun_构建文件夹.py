from pathlib import Path

from pydantic import BaseModel


class PathModel(BaseModel):
    root_path: str

    material_path: str
    preview_image_path: str
    effect_image_path: str


def fun_构建文件夹(root_path: str) -> PathModel:
    root_path_obj = Path(root_path)

    if root_path_obj.is_absolute() is not True:
        raise IndexError("必须使用绝对路径")

    if len(root_path_obj.parts) <= 3:
        raise IndexError("必须使用3层以上的深度目录")

    if root_path_obj.stem == root_path_obj.parent.stem:
        raise IndexError("素材根目录不能和父目录同名")

    if root_path_obj.exists() is False:
        root_path_obj.mkdir()

    material_path = root_path_obj / root_path_obj.stem

    if material_path.exists() is False:
        material_path.mkdir()

    preview_image_path = root_path_obj / "预览图"

    if preview_image_path.exists() is False:
        preview_image_path.mkdir()

    effect_image_path = root_path_obj / "效果图"
    if effect_image_path.exists() is False:
        effect_image_path.mkdir()

    return PathModel(
        root_path=root_path,
        material_path=material_path.as_posix(),
        preview_image_path=preview_image_path.as_posix(),
        effect_image_path=effect_image_path.as_posix(),
    )
