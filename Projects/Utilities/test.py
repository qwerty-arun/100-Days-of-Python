# interact with user -> input
# personalised self-intro

import datetime

name = input("Name: ").strip()
age = input("Age: ").strip()
city = input("Where do you live(city)?: ").strip()
profession = input("What is your profession?: ").strip()
hobby = input("What is your favorite hobby?: ")

intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}.\n"
    f"I work as a {profession} and I absolutely enjoy {hobby}.\n"
    f"Nice to meet you!\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = '*' * 60
final_output = f"{border}\n{intro_message}\n{border}"

print(final_output)