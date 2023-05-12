from module_excel import *

if __name__ == '__main__':
    mainApp = CreateExcel()
    mainApp.start()

# Structure:
# DONE: - Module log: logging
# DONE: - Module date: get current month, get list of working days
# ADDED: - File with constants 'vars.py'
# ADDED: - Test functions
# DONE: - Module: get list of rendered services from file
# DONE: - Module: Allocation of rendered services by days and time
# DONE: - Module: Total time counter
# DONE: - Module: Formation of timesheet, passing it to the Excel module
# DONE: - Module: Formation of excel file(s)
# TODO: - Module: main pivot table on all services by all clients
# TODO: - test cases and logging
