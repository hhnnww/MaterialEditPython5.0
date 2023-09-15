from pydantic import BaseModel


class PicLayoutRatio(BaseModel):
    line_col: int
    ratio: float


def fun_计算各种布局的小图比例(
    line: int, line_col: int, bg_width: int, bg_height: int
) -> float:
    small_im_height = bg_height / line
    small_im_width = bg_width / line_col

    return small_im_width / small_im_height


def fun_构建所有布局小图比例列表(
    line: int, bg_width: int, bg_height: int
) -> list[PicLayoutRatio]:
    pl = []
    for x in range(1, 9):
        pl.append(
            PicLayoutRatio(
                line_col=x,
                ratio=fun_计算各种布局的小图比例(
                    line=line,
                    line_col=x,
                    bg_width=bg_width,
                    bg_height=bg_height,
                ),
            )
        )
    return pl
