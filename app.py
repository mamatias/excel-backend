from typing import Union
from fastapi import FastAPI
from openpyxl import Workbook
from pydantic import BaseModel

class Item(BaseModel):
    dummy : str
    dato1 : Union[str, None] = None
    dato2 : Union[str, None] = None
    dato3 : Union[str, None] = None
    dato4 : Union[str, None] = None
    dato5 : Union[str, None] = None


app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/modelo1/{filename}")
def new_file(filename : str, item :Item):
    workbook = Workbook()
    sheet = workbook.active

    print(item)
    sheet["A1"] = item.dummy
    sheet["B1"] = item.dato1
    sheet["C1"] = item.dato2
    sheet["D1"] = item.dato3
    sheet["E1"] = item.dato4
    sheet["F1"] = item.dato5

    filename_complete = f"{filename}.xlsx"
    workbook.save(filename=filename_complete)

    return {"filename": filename}