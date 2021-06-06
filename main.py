from library import Library
from user import User
from book import Book, Nonfiction

school_library = Library()

#Add users
jane = User("Jane Doe", "jane@example.com")

jakob = User("Jakob Mertens", "jakob@example.co.uk")

mac = User("Mac Bowley", "mac@example.ca")

school_library.add_user(jane)
school_library.add_user(jakob)
school_library.add_user(mac)

#Add books
fault = Book("The Fault in Our Stars", "Young adult novel", "John Green")

hunger_games = Book("The Hunger Games", "Science Fiction", "Suzanne Collins")

name_of_the_wind = Book("The Name of the Wind", "Fantasy", "Patrick Rothfuss")

the_way_of_kings = Book("The Way of Kings", "Fantasy", "Brandon Sanderson")

atomic_habits = Nonfiction("Atomic Habits", "Self help", "James Clear", "Habit Building", "2017")

school_library.add_book(fault)
school_library.add_book(hunger_games)
school_library.add_book(name_of_the_wind)
school_library.add_book(the_way_of_kings)
school_library.add_book(atomic_habits)

# Display Library

school_library.list_books_author()

name_of_the_wind.rent_out(mac)
atomic_habits.rent_out(jane)

print(jane.get_current_book().get_title())