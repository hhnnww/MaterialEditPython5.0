from pathlib import Path

from PIL import Image


def fun_获取单个水印(width: int, fill: tuple[int, int, int, int]) -> Image.Image:
    """
    获取单个水印图片
    可以指定颜色和大小

    Returns:
        Image.Image -- 水印图片
    """
    logo_path = Path(__file__).parent / "logo.png"
    logo_pil = Image.open(logo_path.as_posix())

    with Image.new("RGBA", logo_pil.size, fill) as bg:
        logo_pil.paste(bg, (0, 0), logo_pil)
        logo_pil.thumbnail((width, width), resample=Image.LANCZOS)

    return logo_pil
