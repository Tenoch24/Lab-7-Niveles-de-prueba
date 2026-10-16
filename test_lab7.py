import book
import pytest
import library
import user

@pytest.mark.unit
def test_borrow_book():
    book1 = book.Book("Orgullo y Prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y Prejuicio"
    book1.borrow()
    assert book1.borrowed == True

@pytest.mark.unit
def test_borrow_two_times_book():
    book1 = book.Book("Orgullo y Prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y Prejuicio"
    book1.borrow()
    assert book1.borrowed == True
    with pytest.raises(ValueError,match="The book is already borrowed"):
        book1.borrow()

@pytest.mark.unit
def test_return_book():
    book1 = book.Book("Orgullo y Prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y Prejuicio"
    book1.borrow()
    assert book1.borrowed == True
    book1.return_book()
    assert book1.borrowed == False

@pytest.mark.unit
def test_borrow_and_try_Except():
    book1 = book.Book("Orgullo y Prejuicio", "Tenoch M.", 2026, "ISBN001")
    assert book1.title == "Orgullo y Prejuicio"
    book1.borrow()
    assert book1.borrowed == True
    with pytest.raises(ValueError,match="The book is already borrowed"):
        book1.borrow()

    @pytest.fixture
    def lib_init():
        lib = library.Library()
        book_tenoch = book.Book("Orgullo y Prejuicio", "Tenoch M.", 2026, "ISBN001")
        lib.add_book(book_tenoch)
        Tenoch = user.User("Tenoch", "00001")
        lib.add_user(Tenoch)
        return lib

    @pytest.mark.system
    def test_library_init(lib_init):
        lib = lib_init
        lib.borrow_book("00001", "ISBN001")
        assert lib.books[0].borrowed == True

    @pytest.mark.wip
    def test_library_init_ID_not_register(lib_init):
        lib = lib_init
        
        with pytest.raises(ValueError, match="User not found"):
            lib.borrow_book("00003", "ISBN001")