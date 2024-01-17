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
from users.models import *

fake = Faker('ru_RU')  # You can change the locale as needed

def generate_users(num_users):
    # regions = [
    #     'Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Karakalpakstan',
    #     'Namangan', 'Navoiy', 'Qashqadaryo', 'Samarqand', 'Sirdaryo',
    #     'Surxondaryo', 'Tashkent'
    # ]
    
     for i in range(1, num_users + 1):
        user = Usrs(
            name=fake.name(),
            age=random.randint(1, 101),
            # city=random.choice(regions),
        )
        user.save()

#     districts_of_tashkent_city = [
#         "Bektemir",
#         "Chilanzar",
#         "Mirobod",
#         "Mirzo Ulugbek",
#         "Olmazor",
#         "Sergeli",
#         "Shayxontoxur",
#         "Uchtepa",
#         "Yakkasaray",
#         "Yangihayot",
#         "Yashnobod",
#         "Yunusabad",
#     ]

#     tashkent_region = [
#         "Bekabad",
#         "Bo'stonliq",
#         "Bo'ka",
#         "Qibray",
#         "Ohangaron",
#         "Oqqo'rg'on",
#         "Parkent",
#         "Piskent",
#         "Quyichirchiq",
#         "Zangiota",
#         "O'rtachirchiq",
#         "Yangiyo'l",
#         "Yuqorichirchiq",
#         "Tashkent",
#     ]

#     andijan_region = [
#         "Andijan",
#         "Asaka",
#         "Baliqchi",
#         "Buvayda",
#         "Izboskan",
#         "Jalolquduq",
#         "Khavodin",
#         "Kurgantepa",
#         "Marhamat",
#         "Oltinko'l",
#         "Paxtaobod",
#         "Qo'rg'ontepa",
#         "Shahrixon",
#         "Xo'jaobod",
#     ]

#     fergana_regon = [
#         "Bag'dod",
#         "Beshariq",
#         "Buvayda",
#         "Dangara",
#         "Fergana",
#         "Furqat",
#         "Oltiariq",
#         "Quva",
#         "Qo'shtepa",
#         "Rishton",
#         "So'x",
#         "Toshloq",
#         "Uchkuprik",
#         "O'zbekistan",
#         "Yozyovon",
#     ]

#     namangan_region = [
#         "Namangan",
#         "Kosonsoy",
#         "Chust",
#         "Mingbuloq",
#         "Norin",
#         "Pop",
#         "To'raqo'rg'on",
#         "Uchqo'rg'on",
#         "Uychi",
#         "Yangiqo'rg'on",
#         "Chortoq",
#     ]

#     sirdaryo_region = [
#         "Guliston",
#         "Sirdaryo",
#         "Boyovut",
#         "Mirzaobod",
#         "Oqoltin",
#         "Sardoba",
#         "Sayxunobod",
#         "Xovos",
#     ]

#     jizzakh_region = [
#         "Djizzakh",
#         "Gallaor",
#         "Baxtiyor",
#         "Forish",
#         "Zafarobod",
#         "Yangiobod",
#         "Yaypan",
#         "Mirza-Yolgon",
#         "Pahtaobod",
#         "Budayoni",
#         "Sangzor",
#     ]

#     samarkand_region = [
#         "Samarkand",
#         "Kattakurgan",
#         "Bulung'ur",
#         "Ishtixon",
#         "Jomboy",
#         "Payariq",
#         "Urgut",
#         "Kattaqo'rg'on",
#         "Kushrabat",
#         "Narpay",
#         "Nurobod",
#         "Pastdargom",
#         "Taylak",
#         "Zafarobod",
#     ]

#     qashqadaryo_region = [
#         "Qarshi",
#         "Shahrisabz",
#         "Beshkent",
#         "G'uzor",
#         "Kitob",
#         "Qamashi",
#         "Yakkabog'",
#         "Kasanki",
#         "Mirishkor",
#         "Nishon",
#         "Shofirkon",
#         "Uzun",
#         "Dehkanabad",
#     ]

#     surhondaryo_region = [
#         "Termez",
#         "Denov",
#         "Boysun",
#         "Sherobod",
#         "Surxon",
#         "Uzun",
#         "Jarqo'rg'on",
#         "Sariosiyo",
#         "Kumkurgan",
#         "Sharmishsay",
#     ]

#     bukhara_region = [
#     "Bukhara",
#     "G'ijduvon",
#     "Kogon",
#     "Romitan",
#     "Peshtan",
#     "Vobkent",
#     "Qorako'l",
#     "Nurota",
#     "Navoiy",
#     "Baxtiyor",
#     "Jondor",
# ]

#     navoi_region = [
#         "Navoi",
#         "Zarafshon",
#         "Karmana",
#         "Nurota",
#         "Kiziltepa",
#         "Konimex",
#         "Navbakhor",
#         "Tomdi",
#         "Uchquduq",
#         "Khatirchi",
#     ]

#     khorezm_region = [
#         "Urgench",
#         "Khiva",
#         "Pitnak",
#         "Hazorasp",
#         "Shovot",
#         "Bog'ot",
#         "Yangiyer",
#         "Yangibozor",
#         "Gurlan",
#         "Tupraqqal'a",
#         "Qushkupir",
#     ]

#     karakalpakstan = [
#         "Amudaryo",
#         "Beruniy",
#         "Chimboy",
#         "Qungrat",
#         "Karakalpak",
#         "Mo'ynoq",
#         "Nukus",
#         "Kegeyli",
#         "Takhiatosh",
#         "Mangit",
#         "Shumanay",
#         "Tamdy",
#         "Turtkul",
#         "Xo'jayli",
#         "Shartepa",
#         "Qorao'zak",
#     ]

#     # for i in range(1, num_users + 1):
#     #     user = Usrs(
#     #         name=fake.name(),
#     #         age=random.randint(1, 101),
#     #         # city=random.choice(regions),
#     #     )
#     #     user.save()

#     # country = Country.objects.get(id=1)
#     # for i in regions:
#     #     region = Region(name=i, country=country)
#     #     region.save()

#     region = Region.objects.get(id=13)
#     for i in districts_of_tashkent_city:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=12)
#     for i in tashkent_region:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=1)
#     for i in andijan_region:
#         district = District(name=i, region=region)
#         district.save()


#     region = Region.objects.get(id=2)
#     for i in bukhara_region:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=3)
#     for i in fergana_regon:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=4)
#     for i in jizzakh_region:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=5)
#     for i in karakalpakstan:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=6)
#     for i in namangan_region:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=7)
#     for i in navoi_region:
#         district = District(name=i, region=region)
#         district.save()

#     region = Region.objects.get(id=8)
#     for i in qashqadaryo_region:
#         district = District(name=i, region=region)
#         district.save()


#     region = Region.objects.get(id=9)
#     for i in samarkand_region:
#         district = District(name=i, region=region)
#         district.save()


#     region = Region.objects.get(id=10)
#     for i in sirdaryo_region:
#         district = District(name=i, region=region)
#         district.save()


#     region = Region.objects.get(id=11)
#     for i in surhondaryo_region:
#         district = District(name=i, region=region)
#         district.save()


#     region = Region.objects.get(id=14)
#     for i in khorezm_region:
#         district = District(name=i, region=region)
#         district.save()


def create_random_place_for_user(user):
    # Get random values for country, region, district, and city
    country = Country.objects.order_by('?').first()
    region = Region.objects.filter(country=country).order_by('?').first()
    district = District.objects.filter(region=region).order_by('?').first()
    city = City.objects.filter(region=region).order_by('?').first()

    # Create a Place instance for the user with the random values
    place = Place.objects.create(
        country=country,
        region=region,
        district=district,
        city=city,
    )

    # Add the user to the place's users
    place.users.add(user)




        

if __name__ == "__main__":
    # num_users_to_generate = 9000  # Change this to the desired number of users
    # generate_users(num_users_to_generate)

    # Assuming you have already created 100 users
    users = Usrs.objects.filter()[1001:]

    # Create a random place for each user
    for user in users:
        create_random_place_for_user(user)
