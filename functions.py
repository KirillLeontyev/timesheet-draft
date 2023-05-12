from vars import *
import re
import os


def check_interger(num, allowfloat=False):
    # True if variable is interger only

    result = False
    if allowfloat:
        if (isinstance(num, int) or isinstance(num, float)) and not (isinstance(num, bool)):
            result = True
    else:
        if isinstance(num, int) and not(isinstance(num, bool)):
            result = True
    return result


def classname(klass):
    # Returns classname of the class

    return f'class {klass.__class__.__name__}: '


def check_services_time(time_start, time_end):
    # Check if services time is in a correct interval

    result = False
    fnc = 'fnc check_services_time: '
    message = ''

    if not check_interger(time_start, True):
        message = f'time_start should be an INT (got {time_start.__class__.__name__} instead)'
    if not check_interger(time_end, True):
        message = f'time_end should be an INT (got {time_end.__class__.__name__} instead)'
    if not (9 <= time_start <= 18):
        message = f'time_start should be between 9.00 and 17.45 (got {time_start} instead)'
    if not (9 <= time_end <= 18):
        message = f'time_start should be between 9.15 and 18.00 (got {time_end} instead)'
    if time_end <= time_start:
        message = f'time_end could not be <= time_start (time_start = {time_start}, time_end = {time_end})'

    if message:
        logging.error(''.join((fnc, message)))
    else:
        result = True

    return result


def check_dinner_time(time_start, time_end):
    # Checks if dinner time (13:00-14:00) is between time_start and time_end
    # Returns correct interval for timesheet or False if *args defined with errors

    result = False
    fnc = 'fnc check_dinner_time: '
    message = ''

    if not check_services_time(time_start, time_end):
        message = 'time_start or time_end defined with an error'

    if message:
        logging.error(''.join((fnc, message)))
    else:
        result = []
        if (WORK_START <= time_start < DINNER_START) and (DINNER_END < time_end <= WORK_END):
            result.append([time_start, DINNER_START])
            result.append([DINNER_END, time_end])
        else:
            # Checks if time_start of time_end enters the dinnertime
            # If so, redefine time_start and time_end
            if DINNER_START <= time_start <= DINNER_END:
                time_start = DINNER_END
                logging.warning(''.join((fnc, f'time_start ({time_start}) occupues a part of DINNER time')))
            if DINNER_START <= time_end <= DINNER_END:
                logging.warning(''.join((fnc, f'time_end ({time_end}) occupues a part of DINNER time')))
                time_end = DINNER_START

            # Double check time_start < time_end after redefining
            if time_end <= time_start:
                result = False
                logging.error(''.join((fnc, 'time start ({time_start}) or time_end ({time_end})'
                                            'occupues a part of DINNER time')))
            else:
                result.append([time_start, time_end])
    return result


# TODO: testcase
def client_fullname(name):
    # Gets client's full name if in DB
    # Returns tuple of both full name if found and input name

    oldname = name.capitalize()
    fnc = 'fnc check_dinner_time: '
    clients = (
        'ООО "Токио Роуп Инжиниринг"',
        'ООО "ДЖОН ВАЙЛИ И СЫНОВЬЯ РУС"',
        'ООО "ВОЛТЕРС КЛУВЕР ФАЙНЭНШЛ СЕРВИСЕЗ РУС"',
        'ФИС Глобал Трейдинг (Германия) ГмбХ',
        'Представительство "Сенопласт Клепш & Ко. ГмбХ"',
        'Церазов К.В.'
    )
    for client in clients:
        if re.findall(name, client, re.IGNORECASE):
            logging.info(''.join((fnc, f'client {name} found ({client})')))
            name = client
        elif re.findall(name, 'nan', re.IGNORECASE):
            logging.info(''.join((fnc, f'empty (NaN) value')))
            name = ''
            oldname = name
        else:
            logging.info(''.join((fnc, f'client {name} not found')))
    return name, oldname


# TODO: testcase
def time_format(hours):
    # Convert INT or FLOAT into string 'HHhMMmin'

    minutes = int(60 * hours)
    if hours >= 1:
        minutes = int(60 * (hours % int(hours)))
    hours = int(hours)
    return f'{hours}ч{minutes:0>2}мин'


# TODO: testcase
def get_xlsx():
    # Returns list of XLSX files, excluding temporary (starting with ~)

    files = os.listdir()
    xls = []
    for file in files:
        if re.findall('.xlsx', file):
            if not re.findall('~', file):
                xls.append(file)
    return xls


# TODO: testcase
def check_cell(worksheet, cell):
    # Checks if target cell contains anything

    if worksheet[cell].value is None:
        return True
    else:
        return False
