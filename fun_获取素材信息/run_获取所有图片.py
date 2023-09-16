from pathlib import Path

from pydantic import BaseModel

from setting import IMAGE_SUFFIX


class ImageModel(BaseModel):
    path: str
    name: str


def run_获取所有图片(path: str) -> list[ImageModel]:
    path_obj = Path(path)

    l = []
    for in_file in path_obj.rglob("*"):
        if in_file.is_file() and in_file.suffix.lower() in IMAGE_SUFFIX:
            l.append(ImageModel(path=in_file.as_posix(), name=in_file.name))

    return l
