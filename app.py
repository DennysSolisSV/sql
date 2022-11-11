from user import User
from database import Database

Database.initialise(database='atadb', user='postgres', password='libertad26', host='localhost')

my_user = User('dennys@gmail.com', 'DDDennys', 'Solis', None)

print(my_user)

my_user.save_to_db()

my__user = User.load_from_db_by_email('dennys@gmail.com')

print(my__user)



# database_one = Database()
# database_two = Database()

# print(database_one.connection_pool)

# database_one.initialise()
# print(database_two.connection_pool)