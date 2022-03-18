# LIBS
from fastapi    import APIRouter
import models


# SERVICE
CarService = APIRouter(
    prefix  = "/car",
    tags    = ["car"]
)

# Read
@CarService.get("/{id}", response_model=models.CarResponse)
def get_car():
    pass

# Write
@CarService.post("/")
def create_car():
    pass