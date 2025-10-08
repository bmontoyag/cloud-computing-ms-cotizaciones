
from pydantic import BaseModel

class ProyectoCreate(BaseModel):
    id_proyecto: str
    nombre_proyecto: str
    cliente: str
    total_proyecto: float = 0
    estado: str | None = None

class ProyectoOut(ProyectoCreate):
    pass

class PresupuestoCreate(BaseModel):
    id_presupuesto: str
    id_proyecto: str
    nombre_presupuesto: str
    total_presupuesto: float = 0

class PresupuestoOut(PresupuestoCreate):
    pass
