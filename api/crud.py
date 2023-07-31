from sqlalchemy.orm import Session
import models


def get_forewords(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Foreword).offset(skip).limit(limit).all()

def get_zitije(db: Session, month: int, day: int):
    return db.query(models.Zitije).filter(models.Zitije.dan == day, models.Zitije.mesec == month).first()

