# cloud-computing-ms-cotizaciones

```mermaid


erDiagram
   erDiagram
    PROYECTO {
        string id_proyecto PK
        string id_usuario
        string id_infraestructura
        string nombre_proyecto
        string id_departamento
        string id_provincia
        string id_distrito
        string id_localidad
        number total_proyecto
        string estado
        string fecha_creacion
        string fecha_ultimo_calculo
        string cliente
        string empresa
        number plazo
        number ppto_base
        number ppto_oferta
        number jornada
    }

    PRESUPUESTO {
        string id_presupuesto PK
        string id_proyecto FK
        string nombre_presupuesto
        string fecha_creacion
        number costo_directo
        number parcial_presupuesto
        number porcentaje_igv
        number monto_igv
        number porcentaje_utilidad
        number monto_utilidad
        number ppto_base
        number ppto_oferta
        number total_presupuesto
        number plazo
        string observaciones
        number numeracion_presupuesto
    }

    TITULO {
        string id_titulo PK
        string id_presupuesto FK
        string id_titulo_padre FK
        string id_titulo_plantilla
        string item
        string descripcion
        number parcial
        string fecha_creacion
        string id_especialidad FK
        number nivel
        number orden
        string tipo
    }

    DETALLE_PARTIDA {
        string id_detalle_partida PK
        string unidad_id FK
        string id_titulo FK
        number metrado
        number precio
        number jornada
        number rendimiento
    }

    COMPOSICION_APU {
        string id_composicion_apu PK
        string id_titulo FK
        string id_rec_comp_apu FK
        number cuadrilla
        number cantidad
        string fecha_creacion
    }

    RECURSO_COMPOSICION_APU {
        string id_rec_comp_apu PK
        string recurso_id FK
        string unidad_id FK
        string nombre
        string especificaciones
        string descripcion
        string fecha_creacion
    }

    RECURSO {
        string recurso_id PK
        string codigo
        string nombre
        string descripcion
        date fecha
        number cantidad
        string unidad_id FK
        number precio_actual
        boolean vigente
        string tipo_recurso_id FK
        string tipo_costo_recurso_id FK
        string clasificacion_recurso_id FK
        boolean activo_fijo
        boolean usado
        array imagenes
        array combustible_ids
        string estado_activo_fijo
    }

    UNIDAD {
        string unidad_id PK
        string nombre
        string descripcion
    }

    ESPECIALIDAD {
        string id_especialidad PK
        string nombre
        string descripcion
    }

    PRECIO_RECURSO_PROYECTO {
        string id_prp PK
        string id_proyecto FK
        string id_rec_comp_apu FK
        number precio
        string fecha_creacion
    }

    RECURSO_PRESUPUESTO {
        string id_recurso_presupuesto PK
        objectid recurso_id FK
        string nombre
    }

    DEPARTAMENTO {
        string id_departamento PK
        string nombre
        string descripcion
    }

    PROVINCIA {
        string id_provincia PK
        string id_departamento FK
        string nombre
        string descripcion
    }

    DISTRITO {
        string id_distrito PK
        string id_provincia FK
        string nombre
        string descripcion
    }

    LOCALIDAD {
        string id_localidad PK
        string id_distrito FK
        string nombre
        string descripcion
    }

    INFRAESTRUCTURA {
        string id_infraestructura PK
        string nombre
        string descripcion
    }

    %% Relaciones
    PROYECTO ||--o{ PRESUPUESTO : "tiene"
    PROYECTO ||--o{ PRECIO_RECURSO_PROYECTO : "tiene_precios"
    PROYECTO }o--|| INFRAESTRUCTURA : "pertenece_a"
    PROYECTO }o--|| DEPARTAMENTO : "ubicado_en"
    PROYECTO }o--|| PROVINCIA : "ubicado_en"
    PROYECTO }o--|| DISTRITO : "ubicado_en"
    PROYECTO }o--o| LOCALIDAD : "ubicado_en"

    PRESUPUESTO ||--o{ TITULO : "contiene"
    TITULO ||--o{ TITULO : "tiene_padre"
    TITULO ||--o| DETALLE_PARTIDA : "tiene_detalle"
    TITULO ||--o{ COMPOSICION_APU : "compuesto_por"
    TITULO }o--|| ESPECIALIDAD : "categorizado_por"

    COMPOSICION_APU }o--|| RECURSO_COMPOSICION_APU : "usa_recurso"
    RECURSO_COMPOSICION_APU }o--|| RECURSO : "referencia"
    RECURSO_COMPOSICION_APU }o--|| UNIDAD : "medido_en"
    RECURSO }o--|| UNIDAD : "medido_en"

    PRECIO_RECURSO_PROYECTO }o--|| RECURSO_COMPOSICION_APU : "precio_para"
    RECURSO_PRESUPUESTO }o--|| RECURSO : "referencia"

    DEPARTAMENTO ||--o{ PROVINCIA : "contiene"
    PROVINCIA ||--o{ DISTRITO : "contiene"
    DISTRITO ||--o{ LOCALIDAD : "contiene"


```
