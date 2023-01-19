from fastapi import FastAPI

import uvicorn

from app.models import Base
from app.database import engine
from app.routers import post, user, auth, vote


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
