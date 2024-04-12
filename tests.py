import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
NAMES = ['Ужасы нашего городка', 'Король Лев', 'Абракадабра', 'Гордость и предубеждение и зомби', 'Где моя тачка, чувак!?', 'Что делать, если ваш кот хочет вас убить']
BOOKS = {'Ужасы нашего городка': 'Ужасы', 'Король Лев': 'Мультфильмы', 'Абракадабра': 'Фантастика', 'Гордость и предубеждение и зомби': 'Ужасы', 'Где моя тачка, чувак!?' : 'Комедии', 'Что делать, если ваш кот хочет вас убить': 'Комедии'}

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_books_negative_result(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить, после чего воскресить, укусить, отпустить, потом догнать и снова убить')
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    # напиши свои тесты ниже
    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Король Лев', 'Мультфильмы']])
    def test_set_book_genre_add_books_with_genre_positive_result(self, name, genre):

        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name, genre', [['', 'Ужасы'], ['Король Лев', 'Абракадабра']])
    def test_set_book_genre_add_books_with_unknown_genre(self, name, genre):

        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == '' or not collector.get_book_genre(name)

    def test_get_books_with_specific_genre_add_scary_genre_find_count_two(self):

        collector = BooksCollector()
        for i, k in BOOKS.items():
            collector.add_new_book(i)
            collector.set_book_genre(i, k)
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    @pytest.mark.parametrize('genre', ['', 'Детектив'])
    def test_get_books_with_specific_genre_find_unknown_genre_zero_result(self, genre):

        collector = BooksCollector()
        for i, k in BOOKS.items():
            collector.add_new_book(i)
            collector.set_book_genre(i, k)
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    @pytest.mark.parametrize('name', ['Король Лев', 'Где моя тачка, чувак!?'])
    def test_add_book_in_favorites_add_book_positive_result(self, name):

        collector = BooksCollector()
        for i in NAMES:
            collector.add_new_book(i)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_get_books_for_children_books_without_genre_age_rating_positive_result(self):

        collector = BooksCollector()
        for i, k in BOOKS.items():
            collector.add_new_book(i)
            collector.set_book_genre(i, k)
        for i in ('Король Лев', 'Абракадабра', 'Где моя тачка, чувак!?', 'Что делать, если ваш кот хочет вас убить'):
            assert i in collector.get_books_for_children()

    def test_add_book_in_favorites_add_unknown_book_not_added(self):

        collector = BooksCollector()
        for i in NAMES:
            collector.add_new_book(i)
        collector.add_book_in_favorites('Чебурашка')
        assert 'Чебурашка' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):

        collector = BooksCollector()
        for i in NAMES:
            collector.add_new_book(i)
        collector.add_book_in_favorites('Абракадабра')
        collector.add_book_in_favorites('Король Лев')
        collector.delete_book_from_favorites('Абракадабра')
        assert 'Абракадабра' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_unknown_book_after_add_two_books_count_two(self):

        collector = BooksCollector()
        for i in NAMES:
            collector.add_new_book(i)
        collector.add_book_in_favorites('Абракадабра')
        collector.add_book_in_favorites('Король Лев')
        collector.delete_book_from_favorites('Еще')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_add_two_books(self):

        collector = BooksCollector()
        for i in NAMES:
            collector.add_new_book(i)
        collector.add_book_in_favorites('Абракадабра')
        collector.add_book_in_favorites('Король Лев')
        assert 'Абракадабра' and 'Король Лев' in collector.get_list_of_favorites_books()

    def test_get_books_genre(self):

        collector = BooksCollector()
        for i, k in BOOKS.items():
            collector.add_new_book(i)
            collector.set_book_genre(i, k)
        assert BOOKS == collector.get_books_genre()

    def test_get_book_genre(self):

        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert 'Ужасы'== collector.get_book_genre('Гордость и предубеждение и зомби')



