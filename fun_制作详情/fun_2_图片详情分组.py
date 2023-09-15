from .type import ImageModel


def fun_图片详情分组(
    image_list: list[ImageModel], line_num: int, line_ratio: float
) -> list[list[ImageModel]]:
    comb_list = []

    in_list = []
    in_ratio = 0
    for num, img in enumerate(image_list):
        in_ratio += img.ratio
        in_list.append(img)

        if in_ratio >= line_ratio or len(in_list) >= line_num:
            cp_in_list = in_list.copy()
            comb_list.append(cp_in_list)

            in_list = []
            in_ratio = 0

        if num + 1 == len(image_list):
            if len(in_list) > 0:
                cp_in_list = in_list.copy()
                comb_list.append(cp_in_list)

    return comb_list
