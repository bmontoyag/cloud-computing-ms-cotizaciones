-- Esquema y tablas (cotizaciones)
CREATE SCHEMA IF NOT EXISTS cotizaciones;

CREATE TABLE IF NOT EXISTS cotizaciones.proyecto(
  id_proyecto VARCHAR(50) PRIMARY KEY,
  nombre_proyecto VARCHAR(150),
  cliente VARCHAR(100),
  total_proyecto NUMERIC DEFAULT 0,
  estado VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS cotizaciones.presupuesto(
  id_presupuesto VARCHAR(50) PRIMARY KEY,
  id_proyecto VARCHAR(50) REFERENCES cotizaciones.proyecto(id_proyecto),
  nombre_presupuesto VARCHAR(150),
  total_presupuesto NUMERIC DEFAULT 0
);
