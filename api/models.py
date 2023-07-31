from sqlalchemy import Column, Integer, String

from database import Base


class Foreword(Base):
    __tablename__ = "forewords"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)

class Zitije(Base):
    __tablename__ = "zitije"

    id = Column(Integer, primary_key=True, index=True)
    dan = Column(Integer)
    mesec = Column(Integer)
    sveci = Column(String)
    stihovi = Column(String)
    rasudjivanje = Column(String)
    sozercanje = Column(String)
    beseda = Column(String)
