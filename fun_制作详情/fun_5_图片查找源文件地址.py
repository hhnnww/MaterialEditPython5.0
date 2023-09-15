from pathlib import Path
from typing import Optional

from setting import MATERIAL_SUFFIX


def fun_图片转换成源文件地址(iamge_path: str, material_path: str) -> Optional[Path]:
    im_part = list(Path(iamge_path).parts)
    ma_part = list(Path(material_path).parts)

    im_part[: len(ma_part)] = ma_part
    im_path = Path("/".join(im_part))

    for ma_suffix in MATERIAL_SUFFIX:
        ma_ori_path = Path(im_path).with_suffix(ma_suffix)
        if ma_ori_path.exists():
            return ma_ori_path
