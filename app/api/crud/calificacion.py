from sqlalchemy.orm import Session
from models import calificacion as models
from schemas import calificacion as schemas

def crear_calificacion(db: Session, data: schemas.CalificacionCreate):
    nueva = models.Calificacion(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def obtener_calificaciones(db: Session):
    return db.query(models.Calificacion).all()