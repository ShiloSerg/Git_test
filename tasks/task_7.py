from faker import Faker
from datetime import datetime
import json
import os

fake = Faker('ru_RU')


def generate_person():
    new_person = [{'name': fake.first_name_male(),
                   'surname': fake.last_name_male(),
                   'login': fake.user_name(),
                   'password': fake.password(),
                   'address': fake.address(),
                   'email': fake.email(),
                   'phone': fake.phone_number(),
                   'register_time': datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}]

    file_name = 'test.json'
    if os.stat(file_name).st_size == 0:
        with open(file_name, 'w', encoding="utf8") as f:
            json.dump(new_person, f, indent=4, ensure_ascii=False)
    else:
        with open(file_name, 'r', encoding="utf8") as f:
            data = json.load(f)
            print(f'В файл записана следующая информация: {new_person}')
            data += new_person
        with open(file_name, 'w', encoding="utf8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    generate_person()
