from sqlalchemy.orm import Session , Depends
from database import SessionLocal
import models, schemas



app = FastAPI()

"""
Crear Sesión
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
Crear Calificacion
"""
@app.post("/calificaciones/", response_model=schemas.CalificacionResponse)
def crear_calificacion(data: schemas.CalificacionCreate, db: Session = Depends(get_db)):
    nueva = models.Calificacion(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

"""
Obtener todas
"""
@app.get("/calificaciones/", response_model=list[schemas.CalificacionResponse])