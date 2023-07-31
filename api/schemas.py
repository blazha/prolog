from pydantic import BaseModel


class ForewordBase(BaseModel):
    id: int
    text: str | None = None


class Foreword(ForewordBase):
    class Config:
        orm_mode = True

class ZitijeBase(BaseModel):
    id: int
    dan: int = 1
    mesec: int = 1
    sveci: str = ""
    stihovi: str = ""
    rasudjivanje: str = ""
    sozercanje: str = ""
    beseda: str = ""

class Zitije(ZitijeBase):
    class Config:
        orm_mode = True
