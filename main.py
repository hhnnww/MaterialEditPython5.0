from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from router.router_制作详情 import router as router_制作详情

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router=router_制作详情)
