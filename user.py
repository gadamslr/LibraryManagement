class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.history = []
    self.current_book = None
  
  def set_name(self, user_name):
    user_name = user_name.capitalize()
    self.user = user_name
  
  def get_name(self):
    return self.name
  
  def set_email(self, user_email):
    self.email = user_email
  
  def get_email(self):
    return self.email

  def get_current_book(self):
    return self.current_book
  
  def receive_book(self, book):
      self.current_book = book
  
  def return_book(self):
    self.history.append(self.current_book)
    self.current_book = None
