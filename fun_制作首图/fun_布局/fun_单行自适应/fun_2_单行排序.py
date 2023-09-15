from ..type import PICModel, PicOneLineModel


def fun_2_单行排序(
    line_list: list[PicOneLineModel], line: int, bg_width: int, bg_height: int
) -> list[PicOneLineModel]:
    line_height = bg_height / line
    line_ratio = bg_width / line_height
    line_list = line_list.copy()
    line_list.sort(key=lambda k: abs(line_ratio - k.ratio), reverse=False)
    return line_list
