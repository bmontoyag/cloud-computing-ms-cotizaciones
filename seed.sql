
-- Esquema y tabla para cotizaciones
CREATE SCHEMA IF NOT EXISTS cotizaciones;
CREATE TABLE IF NOT EXISTS cotizaciones.cotizaciones (
  id SERIAL PRIMARY KEY,
  cliente VARCHAR(160) NOT NULL,
  proyecto VARCHAR(160) NOT NULL,
  total NUMERIC DEFAULT 0
);
