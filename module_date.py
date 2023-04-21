from functions import *
import datetime as dt
import calendar as c


class BaseClass:
    # Base class getting year and month
    def __init__(self, year=0, month=0):
        self.today = dt.date.today()
        # If year is not specified, use current instead

        if year == 0:
            self.year = self.today.year
        else:
            # If error in type/value of the year, use current instead
            try:
                self.year = self._check_year_or_month(year)
            except (TypeError, ValueError):
                message = 'Error in type/value of month, current is used'
                logging.warning(''.join((classname(self), message)))
                self.year = self.today.year

        # If month is not specified, use current instead
        if month == 0:
            self.month = self.today.month
        else:
            # If error in type/value of the month, use current instead
            try:
                self.month = self._check_year_or_month(month, 'month')
                logging.info(''.join((classname(self), f'{month} is used')))
            except (TypeError, ValueError):
                message = 'Error in type/value of month, current is used'
                logging.warning(''.join((classname(self), message)))
                self.month = self.today.month

    def _check_year_or_month(self, num=0, numtype='year'):
        # Value check of input 'year' or 'month'
        if check_interger(num):
            if numtype == 'year':
                if num in RANGE_YEARS:
                    return num
                else:
                    message = f'Year should be an INT in range between 2023 and 2023 (got {num} instead)'
                    logging.warning(''.join((classname(self), message)))
                    raise ValueError(message)
            elif numtype == 'month':
                if num in RANGE_MONTHS:
                    return num
                else:
                    message = f'Month should be an INT in range between 1 and 12 (got {num} instead)'
                    logging.warning(''.join((classname(self), message)))
                    raise ValueError(message)
        else:
            wrong_type = num.__class__.__name__
            message = f'Year/Month should be an INT value (got {wrong_type} instead)'
            logging.warning(''.join((classname(self), message)))
            raise TypeError(message)


class TargetMonth(BaseClass):
    def __init__(self, year=0, month=0):
        super().__init__(year, month)

        self.holidays = Holidays(self.year, self.month)


class Holidays(BaseClass):
    holidays = {
        '2023': (
            (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1),
            (23, 2), (24, 2),
            (8, 3),
            (1, 5), (8, 5), (9, 5),
            (12, 6),
            (6, 11)
        )
    }
    shortdays = {
        '2023': (
            (22, 2),
            (7, 3),
            (3, 11)
        )
    }

    def __init__(self, year=0, month=0):
        super().__init__(year, month)

    def get_holidays(self):
        # Returns a set of holidays in given month of the given year
        holidays = []
        for _ in self.holidays[str(self.year)]:
            if _[1] == self.month:
                date = dt.date(self.year, self.month, _[0])
                holidays.append(date)
        logging.info(''.join((classname(self), f'Holidays in {self.month}, {self.year} are set')))
        return set(holidays)

    def get_shortdays(self):
        # Returns a set of short days before holidays in given month of the given year
        shortdays = []
        for _ in self.shortdays[str(self.year)]:
            if _[1] == self.month:
                date = dt.date(self.year, self.month, _[0])
                shortdays.append(date)
        logging.info(''.join((classname(self), f'Shortdays in {self.month}, {self.year} are set')))
        return set(shortdays)

    def get_business_days(self):
        # Returns a list of working days in given month of the given year
        business_days = []
        holidays = self.get_holidays()
        shortdays = self.get_shortdays()
        days_in_month = c.monthrange(self.year, self.month)[1]
        for _ in range(days_in_month):
            date = dt.date(self.year, self.month, _ + 1)
            if dt.datetime.weekday(date) in range(5):
                if date not in holidays:
                    hours = WORKING_HOURS
                    if date in shortdays:
                        hours -= 1
                    business_days.append((date, hours))
        logging.info(''.join((classname(self), f'Business days in {self.month}, {self.year} are set')))
        return business_days
