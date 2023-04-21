from functions import *
import random as r

test_logger = logging.getLogger('functions_TEST')
test_logger.setLevel(COMMON_TEST_LEVEL)
test_handler = logging.FileHandler(f'functions_TEST.log', mode='w')
test_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
test_handler.setFormatter(test_formatter)
test_logger.addHandler(test_handler)

common_test_numbers = list(range(-1000, 3001))
common_test_floats = [_ / 100 for _ in common_test_numbers]
common_test_other = ['string', ('tuple'), ['list'], {'set'}, {'dict': 'test'}, True, False, None, Ellipsis]
common_time_start = [_ for _ in list(range(1,25))]
common_time_end = [_ for _ in list(range(1,25))]
common_time_start_float = [_/10 for _ in list(range(10,250))]
common_time_end_float = [_/10 for _ in list(range(10,250))]
precise_time_start = [_ for _ in list(range(9,19))]
precise_time_end = [_ for _ in list(range(9,19))]
precise_time_start_float = [_/10 for _ in list(range(90,190))]
precise_time_end_float = [_/10 for _ in list(range(90,190))]


class TestFunctions:
    def __init__(self):
        self.methods = [_ for _ in dir(self) if _.startswith('test_')]
        self.completed = 0
        self.failed = 0

    def start(self):
        for method in self.methods:
            print(self.methods.index(method), method)
            if True:
                try:
                    testcase = eval('self.' + method)()
                    self.completed +=1
                except Exception:
                    self.failed += 1
        return self.completed

    def test_check_interger_interger(self):
        '''
        === Test function ===
        Testing: function check_interger
        Test variables: any
        Expected behavior: return True if test var is INT, False otherwise
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_interger(interger) test ===')
        for _ in (common_test_floats + common_test_numbers + common_test_other):
            result = check_interger(_, False)
            message = f'\tinput: {_} | output: {result}'
            test_logger.debug(message)
            if result != default_return:
                exceptions.append((_, result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_interger(interger) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_interger_interget_or_float(self):
        '''
        === Test function ===
        Testing: function check_interger
        Test variables: any
        Expected behavior: return True if test var is INT or FLOAT, False otherwise
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_interger(interger or float) test ===')
        for _ in (common_test_floats + common_test_numbers + common_test_other):
            result = check_interger(_, True)
            message = f'\tinput: {_} | output: {result}'
            test_logger.debug(message)
            if result != default_return:
                exceptions.append((_, result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_interger(interger or float) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_services_time_interger(self):
        '''
        === Test function ===
        Testing: function check_services_time
        Test variables: INT
        Expected behavior: return True if all conditions are met:
            - time_start < time_end
            - 9 <= time_start < 18
            - 9 <= time_end <= 18
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_services_time(int, int) test ===')
        for time_start in (common_time_start):
            for time_end in (common_time_end):
                result = check_services_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if result != default_return:
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(int, int) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_services_time_float(self):
        '''
        === Test function ===
        Testing: function check_services_time
        Test variables: FLOAT
        Expected behavior: return True if all conditions are met:
            - time_start < time_end
            - 9 <= time_start < 18
            - 9 <= time_end <= 18
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_services_time(float, float) test ===')
        for time_start in (common_time_start_float):
            for time_end in (common_time_end_float):
                result = check_services_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if result != default_return:
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(float, float) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_services_time_int_float(self):
        '''
        === Test function ===
        Testing: function check_services_time
        Test variables: time_start = INT, time_end = FLOAT
        Expected behavior: return True if all conditions are met:
            - time_start < time_end
            - 9 <= time_start < 18
            - 9 <= time_end <= 18
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_services_time(int, float) test ===')
        for time_start in (common_time_start):
            for time_end in (common_time_end_float):
                result = check_services_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if result != default_return:
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(int, float) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_services_time_float_int(self):
        '''
        === Test function ===
        Testing: function check_services_time
        Test variables: time_start = FLOAT, time_end = INT
        Expected behavior: return True if all conditions are met:
            - time_start < time_end
            - 9 <= time_start < 18
            - 9 <= time_end <= 18
        Returns: bool
        '''
        default_return = True
        exceptions = []
        test_logger.info('=== check_services_time(float, int) test ===')
        for time_start in (common_time_start_float):
            for time_end in (common_time_end):
                result = check_services_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if result != default_return:
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(float, int) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True
    
    def test_check_dinner_time_int_float(self):
        '''
        === Test function ===
        Testing: function check_dinner_time
        Test variables: time_start = INT in range(9, 19), time_end = FLOAT in range(9.0, 19.0)
        Expected behavior: return list of intervals which could be separated
                            if dinner time is between time_start and time_end
        Returns: list
        '''
        default_return = list
        exceptions = []
        test_logger.info('=== check_services_time(float, int) test ===')
        for time_start in (precise_time_start):
            for time_end in (precise_time_end_float):
                result = check_dinner_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if not isinstance(result, default_return):
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(float, int) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_dinner_time_float_int(self):
        '''
        === Test function ===
        Testing: function check_dinner_time
        Test variables: time_start = FLOAT in range(9.0, 19.0), time_end = INT in range(9, 19)
        Expected behavior: return list of intervals which could be separated
                            if dinner time is between time_start and time_end
        Returns: list
        '''
        default_return = list
        exceptions = []
        test_logger.info('=== check_services_time(float, int) test ===')
        for time_start in (precise_time_start_float):
            for time_end in (precise_time_end):
                result = check_dinner_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if not isinstance(result, default_return):
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(float, int) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True

    def test_check_dinner_time_float_float(self):
        '''
        === Test function ===
        Testing: function check_dinner_time
        Test variables: time_start = FLOAT in range(9.0, 19.0), time_end = FLOAT in range(9.0, 19.0)
        Expected behavior: return list of intervals which could be separated
                            if dinner time is between time_start and time_end
        Returns: list
        '''
        default_return = list
        exceptions = []
        test_logger.info('=== check_services_time(float, float) test ===')
        for time_start in (precise_time_start_float):
            for time_end in (precise_time_end_float):
                result = check_dinner_time(time_start, time_end)
                message = f'\tinput: {time_start, time_end} | output: {result}'
                test_logger.debug(message)
                if not isinstance(result, default_return):
                    exceptions.append(([time_start, time_end], result))
        if exceptions:
            test_logger.info(f'=== main sequence done ===')
            test_logger.info(f'=== {len(exceptions)} exceptions: ===')
            for _ in exceptions:
                test_logger.info(f'\tinput: {_[0]} | output: {_[1]}')
        test_logger.info('=== check_services_time(float, float) test done ===')
        test_logger.info(f'{len(exceptions)} exceptions')
        return True


test_process = TestFunctions()
test_process.start()

finished = f' Tests finished, {test_process.completed}/{len(test_process.methods)} '
failed = f' Tests failed: {test_process.failed} '

blank = '=' * (len(finished) + 6)
br_finished = '=' * 3
br_failed = '=' * int((len(finished) - len(failed) + 6) / 2)

test_logger.info(blank)
test_logger.info(f'{br_finished}{finished}{br_finished}')
test_logger.info(f'{br_failed}{failed}{br_failed}')
test_logger.info(blank)