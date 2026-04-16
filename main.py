from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok", "message": "Kitchen bot API is running"}


@app.post("/calculate-kitchen")
def calculate_kitchen(data: dict):
    length = data.get("length", 0)
    kitchen_type = data.get("kitchen_type", "")
    facade = data.get("facade", "")
    hardware = data.get("hardware", "")
    appliances = data.get("appliances", "")

    price_per_meter = 120000

    if kitchen_type == "corner":
        price_per_meter += 20000
    if facade == "mdf_paint":
        price_per_meter += 30000
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
