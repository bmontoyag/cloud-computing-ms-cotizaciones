
# Cloud Computing - MS Cotizaciones (Fixed for Front)

Rutas usadas por el front:
- GET/POST /api/cotizaciones/proyectos
- GET /api/cotizaciones/presupuestos/{id_proyecto}
- POST /api/cotizaciones/presupuestos

## Configuración
1. Copia `.env.example` a `.env` y completa credenciales.
2. Ejecuta el seed (una sola vez):
```
psql "host=$DB_HOST dbname=$DB_NAME user=$DB_USER password=$DB_PASSWORD port=$DB_PORT sslmode=require" -f seed.sql
```
3. Levanta el servicio:
```
docker compose up -d --build
```
4. Verifica:
- http://<IP>:8081/health
- http://<IP>:8081/docs
- http://<IP>:8081/api/cotizaciones/proyectos

## Notas
- CORS habilitado (abrir en app/util/cors.py para restringir orígenes en prod).
- DB_SCHEMA=cotizaciones con search_path + __table_args__.
