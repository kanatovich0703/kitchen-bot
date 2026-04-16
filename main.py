from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class KitchenRequest(BaseModel):
    length: float
    kitchen_type: str
    facade: str
    hardware: str
    appliances: str


@app.get("/")
def root():
    return {"status": "ok", "message": "Kitchen bot API is running"}


@app.post("/calculate-kitchen")
def calculate_kitchen(data: KitchenRequest):
    length = data.length
    kitchen_type = data.kitchen_type
    facade = data.facade
    hardware = data.hardware
    appliances = data.appliances

    price_per_meter = 120000

    if kitchen_type == "corner":
        price_per_meter += 20000
    elif kitchen_type == "u_shape":
        price_per_meter += 40000

    if facade == "mdf":
        price_per_meter += 30000
    elif facade == "mdf_paint":
        price_per_meter += 50000
    elif facade == "plastic":
        price_per_meter += 40000

    if hardware == "premium":
        price_per_meter += 20000

    if appliances == "yes":
        price_per_meter += 50000

    total_price = length * price_per_meter

    return {
        "price_per_meter": int(price_per_meter),
        "total_price": int(total_price),
        "message": f"Примерная стоимость кухни: {int(total_price)} тг"
    }
