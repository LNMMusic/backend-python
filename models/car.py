# LIBS
from sqlalchemy     import Column, Boolean, ForeignKey, Integer, String
# DB
from db.connection  import Base
from pydantic       import BaseModel


class Car(Base):
    __tablename__ = "cars"

    id          = Column(Integer, primary_key=True, index=True)
    car_name    = Column(String, unique=True, index=True)
    car_plate   = Column(String, unique=True, index=True)

    # Methods
    def Response(self) -> CarResponse:
        return CarResponse(
            self.id,
            self.car_name,
            self.car_plate
        )

class CarResponse(BaseModel):
    id:         str
    car_name:   str
    car_plate:  str