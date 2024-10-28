import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from auth import routes
from auth.models import metadata
from core.database import engine

from .admin import UserAdmin

metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routes.router)

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
