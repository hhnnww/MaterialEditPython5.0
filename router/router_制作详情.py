from fastapi import APIRouter

from fun_制作详情 import MakeProductPageModel, run_制作文件夹详情, run_制作详情

router = APIRouter(prefix="/MakeProductPage")


class RequestMakeProductPageModel(MakeProductPageModel):
    use_preview_image: bool
    use_effect_image: bool

    preview_image_folder: str
    effect_image_folder: str


@router.post("")
def MakeProductPage(item: RequestMakeProductPageModel):
    run_制作文件夹详情(item)
