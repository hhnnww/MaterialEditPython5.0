from pathlib import Path
from typing import Literal

from pydantic import BaseModel


class FontWeightModel(BaseModel):
    light: str
    normal: str
    bold: str
    hevry: str


def fun_获取字体(
    font_name: Literal["opposans", "montserrat", "taibei"] = "opposans",
) -> FontWeightModel:
    """
    根据字体名字,获取字体

    Returns:
        FontWeightModel: 字体模型
    """
    font_path_root = Path(__file__).parent.parent / "font" / font_name

    opposans_name = FontWeightModel(
        light=(font_path_root / "OPPOSans-L.ttf").absolute().as_posix(),
        normal=(font_path_root / "OPPOSans-R.ttf").absolute().as_posix(),
        bold=(font_path_root / "OPPOSans-B.ttf").absolute().as_posix(),
        hevry=(font_path_root / "OPPOSans-H.ttf").absolute().as_posix(),
    )

    montserrat_name = FontWeightModel(
        light=(font_path_root / "montserrat-latin-200-normal.ttf").as_posix(),
        normal=(font_path_root / "montserrat-latin-400-normal.ttf").as_posix(),
        bold=(font_path_root / "montserrat-latin-600-normal.ttf").as_posix(),
        hevry=(font_path_root / "montserrat-latin-700-normal.ttf").as_posix(),
    )

    taibei_name = FontWeightModel(
        light=(font_path_root / "TaipeiSansTCBeta-Light.ttf").as_posix(),
        normal=(font_path_root / "TaipeiSansTCBeta-Light.ttf").as_posix(),
        bold=(font_path_root / "TaipeiSansTCBeta-Regular.ttf").as_posix(),
        hevry=(font_path_root / "TaipeiSansTCBeta-Bold.ttf").as_posix(),
    )

    match font_name:
        case "opposans":
            return opposans_name

        case "montserrat":
            return montserrat_name

        case "taibei":
            return taibei_name
