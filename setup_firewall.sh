#!/bin/bash

# Скрипт для открытия порта 5000 для веб-приложения
# Запускать от root или с sudo

PORT=5000

echo "Открытие порта $PORT..."

# Проверка и использование доступного фаервола
if command -v ufw &> /dev/null; then
    echo "Обнаружен UFW..."
    sudo ufw allow $PORT/tcp
    sudo ufw reload
    echo "Порт $PORT открыт через UFW"
elif command -v firewall-cmd &> /dev/null; then
    echo "Обнаружен firewalld..."
    sudo firewall-cmd --permanent --add-port=$PORT/tcp
    sudo firewall-cmd --reload
    echo "Порт $PORT открыт через firewalld"
elif command -v iptables &> /dev/null; then
    echo "Обнаружен iptables..."
    sudo iptables -A INPUT -p tcp --dport $PORT -j ACCEPT
    sudo iptables-save
    echo "Порт $PORT открыт через iptables"
else
    echo "Фаервол не обнаружен. Возможно, порт уже открыт или фаервол отключен."
fi

echo "Готово!"
