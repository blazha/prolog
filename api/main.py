from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine 

import pdb

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/forewords", response_model=list[schemas.Foreword])
def read_forewords(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    forewords = crud.get_forewords(db, skip=skip, limit=limit)
    return forewords
