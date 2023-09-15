from PIL import Image


def fun_裁剪图片(im: Image.Image, oneline_height: int) -> list[Image.Image]:
    top = 0
    bottom = oneline_height
    if bottom > im.height:
        bottom = im.height
    l = []
    while top < im.height:
        l.append(im.crop((0, top, im.width, bottom)))

        bottom += oneline_height
        top += oneline_height

        if bottom > im.height:
            bottom = im.height

    return l
