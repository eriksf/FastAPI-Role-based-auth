import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from auth import auth, models
from core.database import engine

from .admin import UserAdmin

models.Base.metadata.create_all(bind=engine)


SECRET_KEY = "fb1fd9caaec4e1d22c47552223b421872b159ee980673cdce5dca09c3da1883b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
app.include_router(auth.router)

# ========== admin =======
admin = Admin(app, engine)
admin.add_view(UserAdmin)


@app.get('/')
async def read_home_page():
    return {"msg": "Initialization done"}


if __name__ == "__main__":
    uvicorn.run(
        "core.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True)
