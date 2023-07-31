from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine 

import pdb

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/zitije/{month}/{day}")
def get_zitije(month: int, day: int):
    return {"message": f'zitije na dan {month}-{day}'}
