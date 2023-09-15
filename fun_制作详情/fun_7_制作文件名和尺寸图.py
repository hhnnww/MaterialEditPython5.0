from PIL import Image

from fun_图片处理 import fun_单行字体转图片, fun_图片竖向拼接, fun_获取字体


def fun_制作源文件名字和尺寸信息图片(name_str: str, size_str: str) -> Image.Image:
    info_font_color = (90, 90, 120, 255)
    name_pil = fun_单行字体转图片(
        name_str.upper(),
        en_font_path=fun_获取字体("montserrat").normal,
        cn_font_path=fun_获取字体("opposans").normal,
        fill=info_font_color,
        bg_color=(255, 255, 255, 255),
        size=45,
    )
    size_pil = fun_单行字体转图片(
        size_str.upper(),
        en_font_path=fun_获取字体("montserrat").normal,
        cn_font_path=fun_获取字体("opposans").normal,
        fill=info_font_color,
        bg_color=(255, 255, 255, 255),
        size=35,
    )

    info_pil = fun_图片竖向拼接(
        [name_pil, size_pil],
        10,
        "center",
        background=(255, 255, 255, 255),
    )

    return info_pil
