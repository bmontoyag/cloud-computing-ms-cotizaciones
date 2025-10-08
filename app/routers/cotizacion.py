
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.cotizacion import Proyecto, Presupuesto
from app.schemas.cotizacion import (
    ProyectoCreate, ProyectoOut,
    PresupuestoCreate, PresupuestoOut,
)

router = APIRouter(prefix="/api/cotizaciones", tags=["cotizaciones"])

@router.get("/proyectos", response_model=list[ProyectoOut])
def list_proyectos(db: Session = Depends(get_db)):
    return db.query(Proyecto).all()

@router.post("/proyectos", response_model=ProyectoOut)
def create_proyecto(payload: ProyectoCreate, db: Session = Depends(get_db)):
    exists = db.query(Proyecto).filter_by(id_proyecto=payload.id_proyecto).first()
    if exists:
        raise HTTPException(status_code=409, detail="Proyecto ya existe")
    p = Proyecto(**payload.dict())
    db.add(p)
    db.commit()
    return payload

@router.get("/presupuestos/{id_proyecto}", response_model=list[PresupuestoOut])
def list_presupuestos(id_proyecto: str, db: Session = Depends(get_db)):
    return db.query(Presupuesto).filter_by(id_proyecto=id_proyecto).all()

@router.post("/presupuestos", response_model=PresupuestoOut)
def create_presupuesto(payload: PresupuestoCreate, db: Session = Depends(get_db)):
    if not db.query(Proyecto).filter_by(id_proyecto=payload.id_proyecto).first():
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    pr = Presupuesto(**payload.dict())
    db.add(pr)
    db.commit()
    return payload
