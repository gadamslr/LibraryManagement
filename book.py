class Book:
  def __init__(self, title, genre, author):
    self.title = title
    self.genre = genre
    self.author = author
    self.current_holder = None
  
  def set_title(self, book_title):
    self.title = book_title
  
  def get_title(self):
    return self.title
  
  def set_author(self, book_author):
    book_author = book_author.title()
    self.author = book_author
  
  def get_author(self):
    return self.author
  
  def set_genre(self, book_genre):
    self.genre = book_genre
  
  def get_genre(self):
    return self.genre

  def set_current_holder(self, new_holder):
    self.current_holder = new_holder
  
  def get_current_holder(self):
    return self.current_holder
  
  def rent_out(self, user):
    if user.get_current_book() == None:
      user.receive_book(self)
      self.current_holder = user
    else:
      print(user.get_name() + " already has a book")
  
  def return_book(self):
    self.current_holder.return_book()
    self.current_holder = None
  
class Nonfiction(Book):
  def __init__(self, title, genre, author, topic, year):
    super().__init__(title, genre, author)
    self.topic = topic
    self.year = year
  
  def getTopic(self):
    return self.topic
  
  def setTopic(self, topic):
    self.topic = topic
  
  def getYear(self):
    return self.year
  
  def setYear(self, year):
    self.year = year
