import pandas as pd
from module_date import *

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


# TODO: testcase
# TODO: add logging
class ComposeJobList:
    def __init__(self, filename='services.xlsx', year=2023, month=4):
        self.services = pd.read_excel(filename)
        self.services.columns = ['date', 'time_start', 'time_end', 'service_desc', 'client']
        self.period = TargetMonth(year, month)
        self.joblist = []

    def pd_to_list(self):
        result = []
        for _ in range(len(self.services)):
            service = self.services.loc[_].tolist()
            date = pd.to_datetime(service[0]).date()
            service[0] = date
            result.append(service)
        return result

    def compose(self):
        working_days = self.period.holidays.get_business_days()
        services = self.pd_to_list()
        for day in working_days:
            date = day[0]
            # hours = day[1]
            for service in services:
                if date in service:
                    time_start = float(service[1])
                    time_end = float(service[2])
                    service_desc = service[3]
                    client = service[4]

                    print(client, client.__class__)

                    for _ in check_dinner_time(time_start, time_end):
                        total = _[1] - _[0]
                        client = client_fullname(client)
                        self.joblist.append((date, _[0], _[1], total, service_desc, client))
        return self.joblist
