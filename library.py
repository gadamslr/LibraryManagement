from user import User
from book import Book

class Library:
  def __init__(self):
    self.users = {}
    self.books = []
  
  def add_user(self, new_user):
    self.users[new_user.get_name()] = new_user
  
  def get_user(self, user_name):
    if user_name in self.users:
      return self.users[user_name]
  
  def add_book(self, new_book):
    self.books.append(new_book)
    
  def get_book(self, book_title):
    for book in self.books:
      if book.get_title() == book_title:
        return book
    return None
  
  def list_books_author(self):
    authors = []
    for book in self.books:
      if book.get_author() not in authors:
        print(book.get_author())
        current_author = book.get_author()
        for other in self.books:
          if other.get_author() == current_author:
            print("> " + other.title)
      authors.append(current_author)