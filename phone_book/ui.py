import data_generation as dg
import logger as log
print('Вы открыли телефонный справочник.')

def surname_view(sensor):
    data = dg.get_name(sensor)
    if data is not None:
        name = log.name_logger(data)
        data = dg.get_surname(sensor, name)
        log.surname_logger(data)
        return data
    return None

def phone_view(sensor):
    data = dg.get_phone_number(sensor)
    log.phone_number_logger(data)
    return data

def status_view(sensor):
    phone = phone_view(sensor)
    data = dg.get_status(sensor, phone)
    log.status_logger(data)
    return data