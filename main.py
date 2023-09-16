from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router.router_制作详情 import router as router_制作详情
from router.router_获取图片 import router as router_获取图片
from router.router_获取素材信息 import router as router_获取素材信息

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router=router_制作详情)
app.include_router(router=router_获取素材信息)
app.include_router(router=router_获取图片)
