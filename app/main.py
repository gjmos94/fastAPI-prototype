from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

from fastapi.middleware.cors import CORSMiddleware

print(settings.database_password)
# models.Base.metadata.create_all(bind=engine)   #<-- not needed thanks to alembic generating tables

# use command --> uvicorn app.main:app --reload
# to run app with auto reloading flag

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#including routers for functions
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")       # Path operation  (This decorator makes the following function work with the API with the @)
def root():
    return {"message": "Greetings, and Welcome to the matrix B)"}