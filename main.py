from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class KitchenRequest(BaseModel):
    length: float          # погонные метры
    facade: str            # "лдсп", "мдф", "мдф краска"
    hardware: str          # "стандарт", "премиум"
    closers: str           # "да", "нет"


@app.get("/")
def root():
    return {"status": "ok", "message": "Калькулятор кухни работает"}


@app.post("/calculate-kitchen")
def calculate_kitchen(data: KitchenRequest):
    length = data.length
    facade = data.facade.strip().lower()
    hardware = data.hardware.strip().lower()
    closers = data.closers.strip().lower()

    # Базовая цена за м.п.
    base_price_per_meter = 120000

    # Фасад
    facade_extra = 0
    facade_name = "ЛДСП"

    if facade == "лдсп":
        facade_extra = 0
        facade_name = "ЛДСП"
    elif facade == "мдф":
        facade_extra = 30000
        facade_name = "МДФ"
    elif facade == "мдф краска":
        facade_extra = 50000
        facade_name = "МДФ краска"
    else:
        facade_extra = 0
        facade_name = data.facade

    # Фурнитура
    hardware_extra = 0
    hardware_name = "Стандарт"

    if hardware == "стандарт":
        hardware_extra = 0
        hardware_name = "Стандарт"
    elif hardware == "премиум":
        hardware_extra = 20000
        hardware_name = "Премиум"
    else:
        hardware_extra = 0
        hardware_name = data.hardware

    # Доводчики
    closers_extra = 0
    closers_name = "Нет"

    if closers == "да":
        closers_extra = 15000
        closers_name = "Да"
    elif closers == "нет":
        closers_extra = 0
        closers_name = "Нет"
    else:
        closers_extra = 0
        closers_name = data.closers

    # Итог за м.п.
    final_price_per_meter = (
        base_price_per_meter
        + facade_extra
        + hardware_extra
        + closers_extra
    )

    total_price = final_price_per_meter * length

    message = (
        f"Расчет кухни ({length} м.п.)\n\n"
        f"Стоимость за 1 м.п.: {base_price_per_meter:,} тг\n"
        f"Фасад: {facade_name} (+{facade_extra:,} тг/м.п.)\n"
        f"Фурнитура: {hardware_name} (+{hardware_extra:,} тг/м.п.)\n"
        f"Доводчики: {closers_name} (+{closers_extra:,} тг/м.п.)\n\n"
        f"Итоговая цена за 1 м.п.: {final_price_per_meter:,} тг\n"
        f"Общая примерная стоимость: {int(total_price):,} тг\n\n"
        f"Точную стоимость определит наш замерщик на месте измерив точную длину кухни."
    ).replace(",", " ")

    return {
        "length": length,
        "base_price_per_meter": int(base_price_per_meter),
        "facade_name": facade_name,
        "facade_extra": int(facade_extra),
        "hardware_name": hardware_name,
        "hardware_extra": int(hardware_extra),
        "closers_name": closers_name,
        "closers_extra": int(closers_extra),
        "final_price_per_meter": int(final_price_per_meter),
        "total_price": int(total_price),
        "message": message
    }
