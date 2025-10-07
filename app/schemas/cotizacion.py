
from pydantic import BaseModel

class CotizacionCreate(BaseModel):
    cliente: str
    proyecto: str
    total: float = 0.0

class CotizacionOut(CotizacionCreate):
    id: int
    class Config:
        from_attributes = True
