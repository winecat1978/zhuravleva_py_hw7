import random

from ui import phone_view, status_view, surname_view

def get_name(sensor):
    if sensor:
        male_names = ['Sergey','Michael','Stepan','Alexandr','Dmitriy','Petr','Nickolay','Eugene']
        fe_names = ['Katarina','Lubov','Maria','Vera','Nadezhda','Polina','Luisa','Tatiana']
        n = random.randint(1,2)
        name = ''
        if n == 1:
            name = random.choice(male_names)
        else:
            name = random.choice(fe_names)
        sensor = False
        return name 

def get_surname(sensor,name):
    if sensor:
        surnames = ['Zhuravlev', 'Tomashevich', 'Kuvshinov', 'Makarov', 'Sundukov', 'Danilov','Sergeev','Konstantinov']
        surname = random.choice(surnames)
        if name.endswith('a') or name.endswith('v'):
            if surname.endswith('v'):
                surname = surname + 'a'
        return surname
    else:
        return 0

def get_phone_number(sensor):
    if sensor:
        n = random.randint(1,2)
        phone_num = ''
        if n == 1:
            phone_num = random.randint(79160000000,79999999999)
        else:
            phone_num = random.randint(84950000000,84999999999)
        return phone_num

def get_status(sensor,phone_num):
    if sensor:
        status = ''
        if phone_num > 79159999999 and phone_num < 80000000000:
            status = 'mobile'
        else:
            status = 'work'
    return status

def get_collection(sensor):
    name = get_name(sensor)
    surname = get_surname(sensor,name)
    phone_number = get_phone_number(sensor)
    status = get_status(sensor,phone_number)
    surname_view(sensor)
    phone_view(sensor)
    status_view(sensor)
    return(name,surname,phone_number,status)
