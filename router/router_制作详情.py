from fastapi import APIRouter
from pydantic import BaseModel

from fun_制作详情 import MakeXQModel, run_制作文件夹详情, run_制作详情

router = APIRouter(prefix="/MakeXQ")


@router.post("")
def MakeXQ(item: MakeXQModel):
    pass
