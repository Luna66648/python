# Book API

API для управления книгами и категориями.

## Запуск проекта

```bash
# 1. Клонируем репозиторий
git clone https://github.com/Luna66648/python.git
cd python

# 2. Создаём виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 3. Устанавливаем библиотеки
pip install -r requirements.txt

# 4. Создаём файл .env с настройками БД
cat > .env << EOF
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
EOF

# 5. Создаём базу данных PostgreSQL
sudo -u postgres psql << EOF
CREATE USER octagon WITH PASSWORD '12345';
CREATE DATABASE octagon_db OWNER octagon;
GRANT ALL PRIVILEGES ON DATABASE octagon_db TO octagon;
EOF

# 6. Заполняем базу данными
python -m app.init_db

# 7. Запускаем сервер
uvicorn app.main:app --reload
