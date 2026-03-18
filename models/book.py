"""
Модель книги для личной библиотеки.

Содержит информацию о книге: название, автор, год издания и статус чтения.
"""

from datetime import datetime


class Book:
    """
    Класс, представляющий книгу в библиотеке.
    
    Attributes:
        id (int): Уникальный идентификатор книги
        title (str): Название книги
        author (str): Автор книги
        year (int): Год издания
        status (str): Статус чтения (планирую/читаю/прочитано)
        created_at (datetime): Дата добавления в библиотеку
    """
    
    def __init__(self, id=None, title="", author="", year=0, status="планирую"):
        """
        Инициализация книги.
        
        Args:
            id (int, optional): Уникальный идентификатор
            title (str): Название книги
            author (str): Автор книги
            year (int): Год издания
            status (str): Статус чтения
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status  # планируемо, читаю, прочитано
        self.created_at = datetime.now()
    
    def to_dict(self):
        """
        Преобразует объект книги в словарь.
        
        Returns:
            dict: Словарь с данными книги
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Создает объект книги из словаря.
        
        Args:
            data (dict): Словарь с данными книги
            
        Returns:
            Book: Объект книги
        """
        book = cls(
            id=data.get('id'),
            title=data.get('title', ''),
            author=data.get('author', ''),
            year=data.get('year', 0),
            status=data.get('status', 'планирую')
        )
        return book
    
    def __repr__(self):
        """
        Строковое представление книги.
        
        Returns:
            str: Информация о книге
        """
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"
