from sqlalchemy.orm import Session
import models


def get_forewords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Foreword).offset(skip).limit(limit).all()

