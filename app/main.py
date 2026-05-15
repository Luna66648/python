from fastapi import FastAPI
from app.api import books, categories

app = FastAPI(title="Book API", description="API для управления книгами и категориями")

# Подключаем роутеры
app.include_router(books.router)
app.include_router(categories.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}
