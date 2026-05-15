from app.db.db import SessionLocal, engine, Base
from app.db import crud, models

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    
    try:
        # Проверяем, есть ли уже категории
        if not crud.get_categories(db):
            # Создаём категории
            fiction = crud.create_category(db, "Художественная литература")
            science = crud.create_category(db, "Научная литература")
            
            # Добавляем книги в категорию "Художественная литература"
            crud.create_book(db, "Мастер и Маргарита", "Роман Михаила Булгакова", 500, "", fiction.id)
            crud.create_book(db, "Преступление и наказание", "Роман Фёдора Достоевского", 450, "", fiction.id)
            crud.create_book(db, "Война и мир", "Роман-эпопея Льва Толстого", 800, "", fiction.id)
            
            # Добавляем книги в категорию "Научная литература"
            crud.create_book(db, "Краткая история времени", "Стивен Хокинг о космологии", 600, "", science.id)
            crud.create_book(db, "Будущее разума", "Митио Каку об искусственном интеллекте", 550, "", science.id)
            
            print("База данных успешно заполнена!")
        else:
            print("Категории уже существуют, пропускаем инициализацию.")
            
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
