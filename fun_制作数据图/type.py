from pydantic import BaseModel


class OneLineInfoModel(BaseModel):
    title: str
    desc: str
