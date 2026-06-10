from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import engine, get_db
from schemas import TransactionCreate, Transaction
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Financeira no ar!"}

@app.get("/health")
def health():
    return {"message": "ok"}

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()

@app.post("/transactions", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(
        descricao=transaction.descricao,
        valor=transaction.valor,
        categoria=transaction.categoria,
        data=transaction.data
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.delete("/transactions/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    db.delete(transaction)
    db.commit()
    return {"message": "id apagado"}

@app.put("/transactions/{id}")
def update_transaction(id: int, dados_novos: TransactionCreate, db: Session = Depends(get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    transaction.descricao = dados_novos.descricao
    transaction.valor = dados_novos.valor
    transaction.categoria = dados_novos.categoria
    transaction.data = dados_novos.data
    db.commit()
    return {"message": "update success"}

@app.get("/transactions/summary")
def get_summary(db: Session = Depends(get_db)):
    total_gasto = db.query(func.sum(models.Transaction.valor)).scalar()
    total_transacoes = db.query(func.count(models.Transaction.id)).scalar()
    por_categoria = db.query(
        models.Transaction.categoria,
        func.sum(models.Transaction.valor)
    ).group_by(models.Transaction.categoria).all()

    return {
        "total_gasto": total_gasto,
        "total_transacoes": total_transacoes,
        "por_categoria": [{"categoria": c, "total": t} for c, t in por_categoria]
    }