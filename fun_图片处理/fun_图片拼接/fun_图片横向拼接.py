from typing import Literal

from PIL import Image

from ..fun_图片删除边框 import fun_删除图片边框


def fun_图片横向拼接(
    pil_list: list[Image.Image],
    spacing: int,
    diection: Literal["start", "center", "end"],
) -> Image.Image:
    """
    图片横向拼接

    Returns:
        _type_: PIL 图片
    """
    width = int(sum([int(pil.width) for pil in pil_list])) + int(
        (len(pil_list) - 1) * spacing
    )
    height = max([int(pil.height) for pil in pil_list])

    bg = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    left, top = 0, 0
    for pil in pil_list:
        match diection:
            case "start":
                pass

            case "center":
                top = int((bg.height - pil.height) / 2)

            case "end":
                top = bg.height - pil.height

        if pil.mode != "RGBA":
            pil = pil.convert("RGBA")

        bg.paste(pil, (left, top), pil)
        left += pil.width + spacing
        pil.close()

    bg = fun_删除图片边框(bg, border_color=(255, 255, 255, 0))

    return bg
