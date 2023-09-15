from PIL import Image, ImageDraw


def fun_制作圆形横框(
    width: int,
    height: int,
    fill: tuple[int, int, int, int],
    bg_color: tuple[int, int, int, int] = (255, 255, 255, 0),
    ratio: int = 3,
) -> Image.Image:
    """
    T500首图中的圆角横框

    Args:
        width: 框框的宽度
        height: 框框的高度
        fill: 填充颜色
        bg_color: 整体图片的背景色，不是框框的颜色
        ratio: 放大倍率，默认为3倍，先放大3倍制作图片，然后缩小，这样可以消除锯齿

    Raises:
        IndexError: 圆角横框的宽度必须大于高度

    Returns:
        Image.Image -- 圆角横框
    """
    if height >= width:
        raise IndexError("高度不能和宽度相等")

    bg = Image.new("RGBA", (width * ratio, height * ratio), bg_color)
    draw = ImageDraw.Draw(bg)

    large_width = width * ratio
    large_height = height * ratio

    # 先画两个圆
    draw.ellipse((0, 0, large_height, large_height), fill=fill)
    draw.ellipse(
        (large_width - large_height, 0, large_width, large_height),
        fill=fill,
    )

    # 画中间的方形
    draw.rectangle(
        (
            int(large_height / 2),
            0,
            int(large_width - (large_height / 2)),
            large_height,
        ),
        fill=fill,
    )

    # 缩小到上面给的尺寸
    bg.thumbnail((width, height), resample=Image.LANCZOS)
    return bg
