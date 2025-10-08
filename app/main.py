
from fastapi import FastAPI
from app.db import engine
from app.models.base import Base
from app.routers import cotizacion
from app.util.cors import add_cors

app = FastAPI(title="Servicio Cotizaciones")

# Crear tablas si no existen (demo)
Base.metadata.create_all(bind=engine)

# CORS para el front
add_cors(app)

@app.get("/health")
def health():
    return {"status": "ok"}

# Rutas
app.include_router(cotizacion.router)
