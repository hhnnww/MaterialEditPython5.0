from PIL import Image

from ..fun_图片处理 import fun_制作圆形横框, fun_单行字体转图片, fun_图片居中粘贴, fun_图片竖向拼接, fun_获取字体


def fun_制作详情标题(title: str, desc: str) -> Image.Image:
    font_color = (90, 90, 120, 255)

    title_pil = fun_单行字体转图片(
        text=title,
        en_font_path=fun_获取字体("montserrat").hevry,
        cn_font_path=fun_获取字体("opposans").hevry,
        bg_color=(255, 255, 255, 0),
        fill=font_color,
        size=80,
    )

    circle_pil = fun_制作圆形横框(title_pil.width + 40, 20, fill=(245, 200, 85, 200))

    width = circle_pil.width
    height = title_pil.height + circle_pil.height - 10
    bg = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    bg.paste(circle_pil, (0, title_pil.height - 10), circle_pil)
    bg.paste(title_pil, (20, 0), title_pil)

    desc_pil = fun_单行字体转图片(
        text=desc,
        en_font_path=fun_获取字体("montserrat").normal,
        cn_font_path=fun_获取字体("opposans").normal,
        bg_color=(255, 255, 255, 0),
        fill=font_color,
        size=30,
    )

    bg = fun_图片竖向拼接(
        [bg, desc_pil],
        spacing=30,
        diection="center",
        background=(255, 255, 255, 255),
    )
    bg = fun_图片居中粘贴(bg, 1500, bg.height, (255, 255, 255, 255))

    wbg = Image.new("RGBA", (bg.width, bg.height + 200), (255, 255, 255, 255))
    wbg.paste(bg, (0, 200), bg)
    return wbg


if __name__ == "__main__":
    fun_制作详情标题(title="效果图", desc="Material Effect 此效果图素材内部提供").show()
