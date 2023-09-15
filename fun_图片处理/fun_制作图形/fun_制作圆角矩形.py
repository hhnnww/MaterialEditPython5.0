from PIL import Image, ImageDraw


def fun_制作圆角矩形(
    width: int,
    height: int,
    diameter: int,
    fill: tuple[int, int, int, int],
    bg_color: tuple[int, int, int, int] = (255, 255, 255, 0),
    ratio: int = 3,
):
    """
    画一个圆角矩形

    Args:
        width: 宽度
        height: 高度
        diameter: 圆角的角度
        fill: 填充颜色
        bg_color: 背景颜色，默认透明色
        ratio: 放大倍率，默认放大3倍然后缩小

    Returns:
        Image.Image -- 透明背景的圆角矩形图像
    """
    bg = Image.new("RGBA", (width * ratio, height * ratio), bg_color)

    draw = ImageDraw.Draw(bg)
    draw.rounded_rectangle(
        (0, 0, width * ratio, height * ratio),
        radius=diameter * ratio,
        fill=fill,
    )

    bg.thumbnail((width, height), resample=Image.LANCZOS)
    return bg


if __name__ == "__main__":
    fun_制作圆角矩形(800, 800, 90, (255, 255, 255, 255)).show()
