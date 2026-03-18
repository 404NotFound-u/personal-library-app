
---
# 📚 Personal Library App

Веб-приложение для управления личной библиотекой книг.

## 🚀 Возможности

- ✅ Добавление, редактирование и удаление книг
- ✅ Поиск по названию и автору
- ✅ Отслеживание статуса чтения (Планирую/Читаю/Прочитано)
- ✅ Адаптивный дизайн
- ✅ Совместимость с Linux-средами

## 📋 Требования

- Python 3.8+
- pip (менеджер пакетов Python)
- Linux/WSL среда (рекомендуется)

## 🛠️ Установка и запуск

### 1. Клонируйте репозиторий:
```bash
git clone https://github.com/404NotFound-u/personal-library-app.git
cd personal-library-app
```

### 2. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Установите зависимости:
```bash
pip install -r requirements.txt
```
### 4. Запустите приложение:
```bash
chmod +x run.sh
./run.sh

# Можно так же напрямую
python app.py
```
### 5. Откройте в браузере:

### 📁 Структура проекта
```
personal-library-app/
├── app.py                      # Основное приложение Flask
├── config.py                   # Конфигурация
├── requirements.txt            # Зависимости
├── setup.py                    # Настройка сборки пакета
├── run.sh                      # Скрипт запуска (Linux)
├── README.md                   # Описание проекта
├── .gitignore                  # Игнорируемые файлы
├── static/                     # Статические файлы
│   ├── css/style.css          # Стили
│   └── js/main.js             # JavaScript
├── templates/                  # HTML шаблоны
│   ├── base.html              # Базовый шаблон
│   ├── index.html             # Главная страница
│   ├── book_detail.html       # Страница книги
│   └── add_edit_book.html     # Форма добавления/редактирования
└── models/                     # Модели данных
    ├── __init__.py
    └── book.py                # Модель книги
```

### 📦 Зависимости

| Пакет | Версия | Назначение |
|:-:|:-:|:-:|
| Flask | 3.0.0 | Веб-фреймворк |
| Flask-SQLAlchemy | 3.1.1 | Работа с базой данных |
| python-dotenv | 1.0.0 | Переменные окружения |
| Werkzeug | 3.0.1 | Утилиты WSGI |

### 👥 Команда

| ФИО | Роль |
|:-:|:-:|
| Федорова Анастасия Андреевна | Разработчик |

### 📄 Лицензия
MIT License

---

### **3. Система сборки (п. 2 Части 2)**

Согласно методичке, для Python-проекта необходимо:
- ✅ Файл `requirements.txt` со списком зависимостей
- ✅ Подключить `setuptools` для сборки пакета

#### 3.1 Файл requirements.txt

```txt
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
Werkzeug==3.0.1
setuptools>=65.0.0
sphinx>=7.0.0
sphinx-rtd-theme>=2.0.0
```
