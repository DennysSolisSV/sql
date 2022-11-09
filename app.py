from user import User

my_user = User('dennys@gmail.com', 'DDennys', 'Solis', None)

# print(my_user)

my_user.save_to_db()

# my__user = User.load_from_db_by_email('dennys@gmail.com')

# print(my__user)