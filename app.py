"""
Personal Library Application
Веб-приложение для управления личной библиотекой книг.

Author: Your Team
Version: 1.0.0
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from models.book import Book
from config import config
import os


def create_app(config_name='default'):
    """
    Factory function для создания Flask приложения.
    
    Args:
        config_name (str): Имя конфигурации
        
    Returns:
        Flask: Настроенное приложение
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Инициализация "базы данных" (список в памяти)
    # В будущем заменим на SQLAlchemy
    app.books_db = []
    app.next_id = 1
    
    # Регистрация маршрутов
    register_routes(app)
    
    return app


def register_routes(app):
    """
    Регистрация всех маршрутов приложения.
    
    Args:
        app: Flask приложение
    """
    
    @app.route('/')
    def index():
        """
        Главная страница - список всех книг.
        
        Поддерживает поиск по названию и автору.
        """
        search_query = request.args.get('search', '')
        
        if search_query:
            # Фильтрация книг по поисковому запросу
            filtered_books = [
                book for book in app.books_db
                if search_query.lower() in book.title.lower() or
                   search_query.lower() in book.author.lower()
            ]
            return render_template('index.html', books=filtered_books, search=search_query)
        
        return render_template('index.html', books=app.books_db, search='')
    
    @app.route('/book/<int:book_id>')
    def book_detail(book_id):
        """
        Страница детального просмотра книги.
        
        Args:
            book_id (int): ID книги
        """
        book = next((b for b in app.books_db if b.id == book_id), None)
        if book is None:
            flash('Книга не найдена', 'error')
            return redirect(url_for('index'))
        return render_template('book_detail.html', book=book)
    
    @app.route('/add', methods=['GET', 'POST'])
    def add_book():
        """
        Добавление новой книги.
        
        GET: Показать форму добавления
        POST: Обработать данные формы
        """
        if request.method == 'POST':
            # Получение данных из формы
            title = request.form.get('title', '').strip()
            author = request.form.get('author', '').strip()
            year = request.form.get('year', 0)
            status = request.form.get('status', 'планирую')
            
            # Валидация
            if not title or not author:
                flash('Название и автор обязательны для заполнения', 'error')
                return redirect(url_for('add_book'))
            
            # Создание новой книги
            new_book = Book(
                id=app.next_id,
                title=title,
                author=author,
                year=int(year) if year else 0,
                status=status
            )
            
            app.books_db.append(new_book)
            app.next_id += 1
            
            flash('Книга успешно добавлена', 'success')
            return redirect(url_for('index'))
        
        return render_template('add_edit_book.html', book=None, action='add')
    
    @app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
    def edit_book(book_id):
        """
        Редактирование книги.
        
        Args:
            book_id (int): ID книги
        """
        book = next((b for b in app.books_db if b.id == book_id), None)
        if book is None:
            flash('Книга не найдена', 'error')
            return redirect(url_for('index'))
        
        if request.method == 'POST':
            # Обновление данных
            book.title = request.form.get('title', '').strip()
            book.author = request.form.get('author', '').strip()
            book.year = int(request.form.get('year', 0)) if request.form.get('year') else 0
            book.status = request.form.get('status', 'планирую')
            
            flash('Книга успешно обновлена', 'success')
            return redirect(url_for('book_detail', book_id=book.id))
        
        return render_template('add_edit_book.html', book=book, action='edit')
    
    @app.route('/book/<int:book_id>/delete', methods=['POST'])
    def delete_book(book_id):
        """
        Удаление книги.
        
        Args:
            book_id (int): ID книги для удаления
        """
        app.books_db = [b for b in app.books_db if b.id != book_id]
        
        flash('Книга удалена', 'success')
        return redirect(url_for('index'))
    
    @app.route('/book/<int:book_id>/status/<new_status>', methods=['POST'])
    def update_status(book_id, new_status):
        """
        Обновление статуса книги.
        
        Args:
            book_id (int): ID книги
            new_status (str): Новый статус
        """
        book = next((b for b in app.books_db if b.id == book_id), None)
        if book:
            book.status = new_status
            flash('Статус обновлен', 'success')
        
        return redirect(url_for('book_detail', book_id=book_id))


# Создание приложения
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    # Запуск приложения
    # Для продакшена использовать gunicorn: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(
        host='0.0.0.0',  # Доступно для всех интерфейсов (Linux-совместимо)
        port=5000,
        debug=True
    )
