# LIBS
from fastapi        import APIRouter
from fastapi        import Depends, HTTPException
from sqlalchemy.orm import Session

from client         import get_db
from models         import Car, CarResponse, CarRequest


# SERVICE
CarService = APIRouter(
    prefix  = "/car",
    tags    = ["car"]
)

# Read
@CarService.get("/{id}", response_model=CarResponse)
async def get_car(id:int, db:Session=Depends(get_db)):
    # Process
    car = db.query(Car).filter(Car.id == id).first()
    if car is None:
        raise HTTPException(status_code=400, detail="Failed to Find Car!")
        
    # Response
    return CarResponse.from_orm(car)


# Write
@CarService.post("/create", response_model=CarResponse)
async def create_car(car:CarRequest, db:Session=Depends(get_db)):
    # Process
    car = car.to_model()
    db.add(car)
    db.commit()
    db.refresh(car)

    # Response
    return CarResponse.from_orm(car)