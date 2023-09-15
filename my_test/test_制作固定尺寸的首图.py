from pathlib import Path
from pprint import pprint

from fun_制作首图 import MakeSTModel, run_单行自适应布局, run_固定尺寸布局
from fun_图片处理 import fun_图片蜘蛛水印


def test_制作固定布局的首图():
    p_l = []
    for p in Path(r"F:\小夕素材\10000-10999\10072\预览图").rglob("*"):
        if p.suffix.lower() in [".png", ".jpg"]:
            p_l.append(p.as_posix())

        if len(p_l) >= 39:
            break

    item = MakeSTModel(
        pic_list=p_l,
        line=4,
        spacing=8,
        bg_width=1500,
        bg_height=1500,
        border_radius=8,
        crop_layout="center",
    )

    im = run_固定尺寸布局(item_in=item)
    im = fun_图片蜘蛛水印(im=im, logo_size=80, line=5, line_num=4)
    print(im.size)
    im.show()


if __name__ == "__main__":
    test_制作固定布局的首图()
