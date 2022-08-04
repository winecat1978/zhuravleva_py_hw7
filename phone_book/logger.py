from datetime import datetime as dt
from time import time as time

def name_logger(data):
    time = dt.now().strftime('%H:%M')
    file = open('phonebook.csv','r')
            # print(data, file.readline())
    lines = file.readlines()
    file.close()
    print(lines[-1], lines)
    if 'name' not in lines[-1]:
        with open('phonebook.csv','a') as file:
            file.write('{};name;{}\n'
                        .format(time,data))
            
        return data
    return None
                   
def surname_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('phonebook.csv','a') as file:
        file.write('{};surname;{}\n'
                    .format(time, data))
                    
def phone_number_logger(data):
    time = dt.now().strftime('%H:%M')
    file = open('phonebook.csv','r')
            # print(data, file.readline())
    lines = file.readlines()
    file.close()
    print(lines[-1], lines)
    if 'phone' not in lines[-1]:
        with open('phonebook.csv','a') as file:
            file.write('{};phone;{}\n'
                        .format(time,data))
            
        return data
    return None

def status_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('phonebook.csv','a') as file:
        file.write('{};status;{}\n\n'
                    .format(time, data))