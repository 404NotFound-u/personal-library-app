#!/bin/bash

# Скрипт запуска приложения Personal Library
# Linux-среды - есть совместимость

echo "🚀 Запуск Personal Library Application..."

# Проверка есть ли Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 не найден. Установите Python 3.8+"
    exit 1
fi

# Создание вир окр если его нет
if [ ! -d "venv" ]; then
    echo "📦 Создание виртуального окружения..."
    python3 -m venv venv
fi

# Активация вир окр
echo "🔧 Активация виртуального окружения..."
source venv/bin/activate

# Установка зависимостей
echo "📥 Установка зависимостей..."
pip install -r requirements.txt

# Запуск приложения
echo "✅ Запуск приложения на http://0.0.0.0:5000"
echo "Для остановки нажмите Ctrl+C"
python app.py
