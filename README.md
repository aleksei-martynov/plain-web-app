# Plain Web App

Простое веб-приложение на Python (FastAPI + Uvicorn), которое выводит приветствие.

## Быстрый старт (локально)

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск приложения
uvicorn app:app --host 0.0.0.0 --port 5000
```

Приложение будет доступно по адресу: http://localhost:5000

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
pip install -r requirements.txt
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
```

### 4. Запуск приложения

```bash
# Простой запуск
uvicorn app:app --host 0.0.0.0 --port 5000

# Для продакшена (с автозапуском через systemd)
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

---

## Доступ к приложению

После запуска приложение будет доступно по адресу:
```
http://<IP-вашего-сервера>:5000
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
