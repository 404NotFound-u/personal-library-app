/**
 * Personal Library Application
 * Основной JavaScript файл
 * 
 * @author Your Team
 * @version 1.0.0
 */

// Инициализация приложения после загрузки DOM
document.addEventListener('DOMContentLoaded', function() {
    console.log('Personal Library App initialized');
    
    // Автоматическое скрытие flash-сообщений через 5 секунд
    const flashMessages = document.querySelectorAll('.flash');
    flashMessages.forEach(function(message) {
        setTimeout(function() {
            message.style.opacity = '0';
            message.style.transition = 'opacity 0.5s';
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 5000);
    });
    
    // Подтверждение удаления книги
    const deleteForms = document.querySelectorAll('form[onsubmit*="confirm"]');
    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(e) {
            if (!confirm('Вы уверены, что хотите удалить эту книгу?')) {
                e.preventDefault();
            }
        });
    });
});

/**
 * Функция для поиска книг (дополнительная функциональность)
 * @param {string} query - Поисковый запрос
 */
function searchBooks(query) {
    if (query.length < 2) {
        return;
    }
    
    console.log('Searching for:', query);
    // Здесь можно добавить AJAX поиск
}
