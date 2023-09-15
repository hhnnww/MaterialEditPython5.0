from PIL import Image, ImageDraw


def fun_画边框(im: Image.Image, border_color: tuple[int, int, int, int]):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0, 0, im.height), fill=border_color, width=1)
    draw.line((0, 0, im.width, 0), fill=border_color, width=1)

    draw.line(
        (im.width - 1, im.height - 1, im.width - 1, 0),
        fill=border_color,
        width=1,
    )

    draw.line(
        (im.width - 1, im.height - 1, 0, im.height - 1),
        fill=border_color,
        width=1,
    )

    return im
