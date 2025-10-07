
from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Cotizacion(Base):
    __tablename__ = "cotizaciones"
    __table_args__ = {"schema": "cotizaciones"}
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    cliente: Mapped[str] = mapped_column(String(160))
    proyecto: Mapped[str] = mapped_column(String(160))
    total: Mapped[float] = mapped_column(default=0.0)
