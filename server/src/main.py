from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.router import router as router_orm


app = FastAPI(
    title="HACK_08_10"
)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_orm)
