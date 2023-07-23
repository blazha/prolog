from pydantic import BaseModel


class ForewordBase(BaseModel):
    id: int
    text: str | None = None


class Foreword(ForewordBase):
    class Config:
        orm_mode = True
