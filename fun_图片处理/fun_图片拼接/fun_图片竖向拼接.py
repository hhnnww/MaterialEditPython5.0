from typing import Literal

from PIL import Image

from ..fun_图片删除边框 import fun_删除图片边框


def fun_图片竖向拼接(
    pil_list: list[Image.Image],
    spacing: int,
    diection: Literal["start", "center", "end"],
    background: tuple[int, int, int, int] = (255, 255, 255, 0),
) -> Image.Image:
    """
    图片竖向拼接

    Returns:
        _type_: PIL 图片
    """
    width = max([int(pil.width) for pil in pil_list])
    height = int(sum([int(pil.height) for pil in pil_list])) + int(
        (len(pil_list) - 1) * spacing
    )

    bg = Image.new("RGBA", (width, height), background)
    left, top = 0, 0
    for pil in pil_list:
        match diection:
            case "start":
                pass

            case "center":
                left = int((bg.width - pil.width) / 2)

            case "end":
                left = bg.width - pil.width

        if pil.mode != "RGBA":
            pil = pil.convert("RGBA")

        bg.paste(pil, (left, top), pil)
        top += pil.height + spacing
        pil.close()

    return bg
