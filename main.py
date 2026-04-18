from fastapi import FastAPI

from routers.vendors import router
app = FastAPI()

app.include_router(router)

