from fastapi import FastAPI

from core.api.sales_person import sales_person_api
from core.api.merchant import merchant_api
from core.database.connection import Base, engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(sales_person_api.router)
app.include_router(merchant_api.router)


@app.get("/")
async def home():
    return {"XPayBack CRM APIs"} 
