from PIL import Image


def fun_图片居中粘贴(
    im: Image.Image,
    width: int,
    height: int,
    background: tuple[int, int, int, int],
):
    with im:
        bg = Image.new("RGBA", (width, height), background)
        left = int((bg.width - im.width) / 2)
        top = int((bg.height - im.height) / 2)
        bg.paste(im, (left, top), im)

    return bg
