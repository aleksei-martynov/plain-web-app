# Plain Web App

Простое веб-приложение на Python (FastAPI + Uvicorn), которое выводит приветствие.

## Быстрый старт (локально)

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/macOS)
source venv/bin/activate

# Установка зависимостей
pip install -e ".[dev]"

# Запуск приложения
uvicorn app:app --host 0.0.0.0 --port 5000
```

Приложение будет доступно по адресу: http://localhost:5000/hello

## Разработка

### Установка dev-зависимостей

```bash
pip install -e ".[dev]"
```

### Запуск линтера и форматтера

```bash
ruff check .        # Проверка кода
ruff format .       # Форматирование кода
```

### Запуск тестов

```bash
pytest
```

### Установка pre-commit хуков

```bash
pre-commit install
```

Теперь перед каждым коммитом код будет автоматически проверяться и форматироваться.

---

## Установка на сервер (Linux)

### 1. Клонирование репозитория

```bash
git clone <URL-вашего-репозитория>
cd plain-web-app
```

### 2. Установка Python и зависимостей

```bash
# Для Ubuntu/Debian
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install -e ".[dev]"
```

### 3. Открытие порта в фаерволе

```bash
# Для UFW (Ubuntu)
sudo ufw allow 5000/tcp
sudo ufw reload

# Для firewalld (CentOS/RHEL)
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload

# Для iptables
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
sudo iptables-save

# Или используй готовый скрипт
chmod +x setup_firewall.sh
./setup_firewall.sh
```

### 4. Запуск приложения

```bash
# Активация окружения
source venv/bin/activate

# Запуск (для разработки)
uvicorn app:app --host 0.0.0.0 --port 5000

# Для продакшена (несколько воркеров)
uvicorn app:app --host 0.0.0.0 --port 5000 --workers 4
```

### 5. Настройка как systemd-сервис (опционально)

Создайте файл `/etc/systemd/system/plain-web-app.service`:

```ini
[Unit]
Description=Plain Web App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/plain-web-app
ExecStart=/path/to/plain-web-app/venv/bin/uvicorn app:app --host 0.0.0.0 --port 5000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
```

Активируйте сервис:

```bash
sudo systemctl daemon-reload
sudo systemctl enable plain-web-app
sudo systemctl start plain-web-app
sudo systemctl status plain-web-app
```

### 6. Проверка работы

Открой в браузере:
```
http://<IP-вашего-сервера>:5000/hello
```

---

## Структура проекта

```
plain-web-app/
├── app.py              # Основное приложение FastAPI
├── requirements.txt    # Зависимости Python
├── templates/
│   └── index.html      # HTML-шаблон
├── README.md           # Эта инструкция
└── setup_firewall.sh   # Скрипт для открытия порта
```
