import json
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine 

from starlette.responses import Response
from starlette.status import HTTP_200_OK

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
    return crud.get_forewords(db, skip=skip, limit=limit)

@app.get("/zitije/{month}/{day}", response_model=schemas.Zitije)
def get_zitije(month: int, day: int, db: Session = Depends(get_db)):
    zitije =  crud.get_zitije(db, month=month, day=day)
    if zitije is None:
        return Response(status_code=HTTP_200_OK, content=json.dumps({}))
    else:
        return zitije
