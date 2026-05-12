from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from crud import calificacion as crud
from schemas import calificacion as schemas
import models.calificacion

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS — permite que el HTML se conecte a la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Agregar calificación
@app.post("/calificaciones/", response_model=schemas.CalificacionResponse)
def crear_calificacion(data: schemas.CalificacionCreate, db: Session = Depends(get_db)):
    return crud.crear_calificacion(db, data)

# Ver todas las calificaciones
@app.get("/calificaciones/", response_model=list[schemas.CalificacionResponse])
def obtener_calificaciones(db: Session = Depends(get_db)):
    return crud.obtener_calificaciones(db)