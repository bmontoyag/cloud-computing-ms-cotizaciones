
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.cotizacion import Cotizacion
from app.schemas.cotizacion import CotizacionCreate, CotizacionOut

router = APIRouter(prefix="/cotizaciones", tags=["cotizaciones"])

@router.get("/", response_model=list[CotizacionOut])
def list_cotizaciones(db: Session = Depends(get_db)):
    return db.query(Cotizacion).all()

@router.post("/", response_model=CotizacionOut)
def create_cotizacion(payload: CotizacionCreate, db: Session = Depends(get_db)):
    c = Cotizacion(**payload.dict())
    db.add(c)
    db.commit()
    db.refresh(c)
    return c
