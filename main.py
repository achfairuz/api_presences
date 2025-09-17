from fastapi import FastAPI
from routes.API import user_routes, device_routes, presence_routes

app = FastAPI(title="Presence Management API")
app.include_router(user_routes.router, prefix="/api", tags=["Users"])
app.include_router(device_routes.router, prefix="/api", tags=["Devices"])
app.include_router(presence_routes.router, prefix="/api", tags=["Presences"])
