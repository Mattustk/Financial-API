from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    descricao: str
    valor: float
    categoria: str
    data: date

class Transaction(TransactionCreate):
    id: int