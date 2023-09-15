from fastapi import FastAPI

from router.router_制作详情 import router as router_制作详情

app = FastAPI()

app.include_router(router=router_制作详情)
