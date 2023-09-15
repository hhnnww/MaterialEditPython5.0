from ..type import PicOneLineModel


def fun_3_确定结构(
    line_list: list[PicOneLineModel], line: int
) -> list[PicOneLineModel]:
    st_list: list[PicOneLineModel] = []

    for x in line_list:
        if len(st_list) > 0:
            if fun_组合已经采用(st_list=st_list, line_comb=x) is True:
                continue

        # 如果没有使用就添加到首图编组
        st_list.append(x)

        # 满足行数后退出循环
        if len(st_list) == line:
            return st_list

    return st_list


def fun_组合已经采用(
    st_list: list[PicOneLineModel], line_comb: PicOneLineModel
) -> bool:
    used_pic = []
    for in_list in st_list:
        for pic in in_list.pic_list:
            used_pic.append(pic.path)

    for line in line_comb.pic_list:
        if line.path in used_pic:
            return True

    return False
