
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Proyecto(Base):
    __tablename__ = "proyecto"
    __table_args__ = {"schema": "cotizaciones"}

    id_proyecto: Mapped[str] = mapped_column(String(50), primary_key=True)
    nombre_proyecto: Mapped[str] = mapped_column(String(150))
    cliente: Mapped[str] = mapped_column(String(100))
    total_proyecto: Mapped[float] = mapped_column(Numeric, default=0)
    estado: Mapped[str | None] = mapped_column(String(30), nullable=True)

class Presupuesto(Base):
    __tablename__ = "presupuesto"
    __table_args__ = {"schema": "cotizaciones"}

    id_presupuesto: Mapped[str] = mapped_column(String(50), primary_key=True)
    id_proyecto: Mapped[str] = mapped_column(String(50), ForeignKey("cotizaciones.proyecto.id_proyecto"))
    nombre_presupuesto: Mapped[str] = mapped_column(String(150))
    total_presupuesto: Mapped[float] = mapped_column(Numeric, default=0)
