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
        self.services.columns = ['date', 'time_start', 'time_end', 'desc', 'client']
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
        # DEPRECATED
        # dates = self.services['date'].dt.date.tolist()

        for day in working_days:
            work_end = WORK_END if day[1] == 8 else WORK_START + day[1] + 1
            day_list = []
            if day[0] in [_[0] for _ in services]:
                for index, service in enumerate(services):
                    if day[0] in service:
                        date = service[0]
                        time_start = service[1]
                        time_end = service[2]
                        desc = service[3]
                        client = service[4]
                        work_end = WORK_START + day[1] + 1
                        time_res = check_dinner_time(float(time_start), float(time_end))

                        if not day_list:
                            # Inserting NPA if service entry is first in list of the day and time start != 9
                            if time_start != WORK_START:
                                npa_res = check_dinner_time(float(WORK_START), float(time_start))
                                for res_start, res_end in npa_res:
                                    day_list.append([date, res_start, res_end, 'Поиск НПА и практики', ''])

                        else:
                            # If service entry is not first in the day list, get previous time_end and insert NPA
                            prev_end = day_list[-1][2]
                            if prev_end != time_start and (prev_end != 13 and time_start != 14):
                                npa_res = check_dinner_time(float(prev_end), float(time_start))
                                for res_start, res_end in npa_res:
                                    day_list.append([date, res_start, res_end, 'Поиск НПА и практики', ''])

                        # Adding service, checking is there a dinner time between time_start and time_end
                        for res_start, res_end in time_res:
                            day_list.append([date, res_start, res_end, desc, client])

                        # If service entry is last in the day list and time_end != 18, insert NPA at the end
                        next_index = services[index]
                        try:
                            next_index = services[index + 1]
                        except IndexError as e:
                            pass
                            # TODO: add logging
                        if next_index[0] != date or next_index == services[index]:
                            print('yes', index, desc, client, date)
                            if time_end != work_end:
                                npa_res = check_dinner_time(float(time_end), float(work_end))
                                for res_start, res_end in npa_res:
                                    day_list.append([date, res_start, res_end, 'Поиск НПА и практики', ''])

            # Insert NPA if no service entries are in the day list
            else:
                day_list.append([day[0], WORK_START, DINNER_START, 'Поиск НПА и практики', ''])
                day_list.append([day[0], DINNER_END, work_end, 'Поиск НПА и практики', ''])
            self.joblist.append([day_list, day[1]])

        # DEBUG entry
        for day_selected, hours in self.joblist:
            if day_selected:
                for job in day_selected:
                    print(job)


        # return self.joblist

    def insert_NPA(self):
        working_days = self.period.holidays.get_business_days()
