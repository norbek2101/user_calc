# Sample user data (you can customize this based on your actual data)
import random

# List of Uzbekistan regions
uzbekistan_regions = [
    'Tashkent', 'Samarkand', 'Bukhara', 'Andijan', 'Namangan',
    'Fergana', 'Navoiy', 'Jizzakh', 'Khorezm', 'Surkhandarya',
    'Karakalpakstan', 'Sirdaryo'
]

# Generate 50 user data entries
user_db = []

for _ in range(50):
    name = f"User{_ + 1}"
    city = random.choice(uzbekistan_regions)
    age = random.randint(18, 50)

    user_data = {'name': name, 'city': city, 'age': age}
    user_db.append(user_data)

def filter_users_by_city(users, city):
    """
    Filter users by city.

    Parameters:
    users (list): List of dictionaries representing users.
    city (str): City to filter users.

    Returns:
    list: List of users in the specified city.
    """
    return [user for user in users if user.get('city') == city]

def main():
    while True:
        # Get user input for the city
        city_input = input("Enter a city (Tashkent/Samarkand/Bukhara/... or 'exit' to quit): ").capitalize()

        # Check if the user wants to exit
        if city_input == 'Exit':
            print("Exiting the program.")
            break

        # Check if the entered city is valid
        if city_input not in uzbekistan_regions:
            print("Invalid city. Please enter a valid Uzbekistan region.")
            continue

        # Filter users based on the entered city
        filtered_users = filter_users_by_city(user_db, city_input)

        # Display the filtered users count
        print(f"Number of users available from {city_input}: {len(filtered_users)}")

if __name__ == "__main__":
    main()
