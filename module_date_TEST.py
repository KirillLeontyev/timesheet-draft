from module_date import *

test_logger = logging.getLogger('module_date_TEST')
test_logger.setLevel(logging.INFO)
test_handler = logging.FileHandler(f'module_date_TEST.log', mode='w')
test_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
test_handler.setFormatter(test_formatter)
test_logger.addHandler(test_handler)

common_test_numbers = list(range(-1000, 3001))
common_test_other = ['string', ('tuple'), ['list'], {'set'}, {'dict': 'test'}, True, False, None, Ellipsis]
precise_test_months = list(range(1, 13))
precise_test_years = [2023]


def test_TargetMonth_year():
    '''
    === Test function ===
    Testing: class TargetMonth, attr year
    Test variables: any
    Expected behavior: Use default year in all cases except test variables are INT in range from 2023 to 2023
    Returns: TargetMonth.year
    '''
    default_return = 2023
    exceptions = []
    test_logger.debug('=== TargetMonth.year test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = TargetMonth(year=_)
        message = f'\tinput: {_} | output: {klass.year}'
        test_logger.debug(message)
        if klass.year != default_return:
            exceptions.append((_, klass.year))
        del klass
    test_logger.debug('=== TargetMonth.year test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True


def test_TargetMonth_month():
    '''
    === Test function ===
    Testing: class TargetMonth, attr month
    Test variables: any
    Expected behavior: Use default month in all cases except test variables are INT in range from 1 to 12
    Returns: TargetMonth.month
    '''
    default_return = 4
    exceptions = []
    test_logger.debug('=== TargetMonth.month test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = TargetMonth(month=_)
        message = f'\tinput: {_} | output: {klass.month}'
        test_logger.debug(message)
        if klass.month != default_return:
            exceptions.append((_, klass.month))
        del klass
    test_logger.debug('=== TargetMonth.month test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True


def test_TargetMonth_year_and_month():
    '''
    === Test function ===
    Testing: class TargetMonth, attr year & month
    Test variables: any
    Expected behavior: Use default month and year in all cases except month in range(1, 13), year in range(2023, 2024)
    Returns: TargetMonth.year, TargetMonth.month
    '''
    default_return_year = 2023
    default_return_month = 4
    exceptions = []
    test_logger.debug('=== TargetMonth.year | TargetMonth.month test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = TargetMonth(year=_, month=_)
        message = f'\tinput: {_} | output: year={klass.year}, month={klass.month}'
        test_logger.debug(message)
        if klass.year != default_return_year:
            exceptions.append((_, klass.year))
        if klass.month != default_return_month:
            exceptions.append((_, klass.month))
        del klass
    test_logger.debug('=== TargetMonth.year | TargetMonth.month test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True


def test_Holidays_year():
    '''
    === Test function ===
    Testing: class Holidays, attr year
    Test variables: any
    Expected behavior: Use default year in all cases except test variables are INT in range from 2023 to 2023
    Returns: Holidays.year
    '''
    default_return = 2023
    exceptions = []
    test_logger.debug('=== Holidays.year test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = Holidays(year=_)
        message = f'\tinput: {_} | output: {klass.year}'
        test_logger.debug(message)
        if klass.year != default_return:
            exceptions.append((_, klass.year))
        del klass
    test_logger.debug('=== Holidays.year test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True


def test_Holidays_month():
    '''
    === Test function ===
    Testing: class Holidays, attr month
    Test variables: any
    Expected behavior: Use default month in all cases except test variables are INT in range from 1 to 12
    Returns: Holidays.month
    '''
    default_return = 4
    exceptions = []
    test_logger.debug('=== Holidays.month test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = Holidays(month=_)
        message = f'\tinput: {_} | output: {klass.month}'
        test_logger.debug(message)
        if klass.month != default_return:
            exceptions.append((_, klass.month))
        del klass
    test_logger.debug('=== Holidays.month test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True


def test_Holidays_year_and_month():
    '''
    === Test function ===
    Testing: class Holidays, attr year & month
    Test variables: any
    Expected behavior: Use default month and year in all cases except month in range(1, 13), year in range(2023, 2024)
    Returns: Holidays.year, Holidays.month
    '''
    default_return_year = 2023
    default_return_month = 4
    exceptions = []
    test_logger.debug('=== Holidays.year | Holidays.month test ===')
    for _ in (common_test_numbers + common_test_other):
        klass = Holidays(year=_, month=_)
        message = f'\tinput: {_} | output: year={klass.year}, month={klass.month}'
        test_logger.debug(message)
        if klass.year != default_return_year:
            exceptions.append((_, klass.year))
        if klass.month != default_return_month:
            exceptions.append((_, klass.month))
        del klass
    test_logger.debug('=== Holidays.year | Holidays.month test done ===')
    test_logger.info(f'{len(exceptions)} exceptions:')
    for _ in exceptions:
        test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
    return True

def test_Holidays_holidays():
    '''
    === Test function ===
    Testing: class Holidays, attr holidays
    Test variables: self.year = 2023, self.month = range(1, 13)
    Expected behavior: Get list of holidays in given month (if any, empty list otherwise)
    Returns: Holidays.holidays
    '''
    test_logger.debug('=== Holidays.holidays test ===')
    for test_year in precise_test_years:
        for test_month in precise_test_months:
            klass = Holidays(month=test_month, year=test_year)
            message = f'\tinput: year={test_year}, month={test_month} | output: holidays={klass.holidays}'
            test_logger.debug(message)
            del klass
    test_logger.debug('=== Holidays.holidays test done ===')
    return True

def test_Holidays_shortdays():
    '''
    === Test function ===
    Testing: class Holidays, attr shortdays
    Test variables: self.year = 2023, self.month = range(1, 13)
    Expected behavior: Get list of shortdays in given month (if any, empty list otherwise)
    Returns: Holidays.shortdays
    '''
    test_logger.debug('=== Holidays.shortdays test ===')
    for test_year in precise_test_years:
        for test_month in precise_test_months:
            klass = Holidays(month=test_month, year=test_year)
            message = f'\tinput: year={test_year}, month={test_month} | output: holidays={klass.shortdays}'
            test_logger.debug(message)
            del klass
    test_logger.debug('=== Holidays.shortdays test done ===')
    return True

tests = [
    test_TargetMonth_year(),
    test_TargetMonth_month(),
    test_TargetMonth_year_and_month(),
    test_Holidays_year(),
    test_Holidays_month(),
    test_Holidays_year_and_month(),
    test_Holidays_holidays(),
    test_Holidays_shortdays()
]
test_logger.debug(f'=================================================')
test_logger.debug(f'=== Tests finished, {sum(tests)}/{len(tests)} ===')
test_logger.debug(f'=================================================')

