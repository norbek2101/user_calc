import django
import sys
import os
# --------- < DJANGO SETUP > -----------
path_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
# --------  < / DJANGO SETUP > -------- 

import random
from faker import Faker


# Now you can import your models
from users.models import Usrs

fake = Faker('tr_TR')  # You can change the locale as needed

def generate_users(num_users):
    regions = [
        'Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Karakalpakstan',
        'Namangan', 'Navoiy', 'Qashqadaryo', 'Samarqand', 'Sirdaryo',
        'Surxondaryo', 'Tashkent'
    ]

    for i in range(1, num_users + 1):
        user = Usrs(
            name=fake.name(),
            age=random.randint(18, 60),
            city=random.choice(regions),
        )
        user.save()

if __name__ == "__main__":
    num_users_to_generate = 500  # Change this to the desired number of users
    generate_users(num_users_to_generate)
