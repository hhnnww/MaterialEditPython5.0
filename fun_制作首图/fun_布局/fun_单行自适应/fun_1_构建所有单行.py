from itertools import combinations

from ..type import PICModel, PicOneLineModel


def fun_1_所有单行(pic_list: list[PICModel], line: int) -> list[PicOneLineModel]:
    all_comb = []
    for x in range(1, line + 4):
        all_comb.extend(
            [
                PicOneLineModel(
                    ratio=sum([p.ratio for p in line]), pic_list=list(line)
                )
                for line in combinations(pic_list, x)
            ]
        )

    return all_comb
