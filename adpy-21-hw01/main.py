from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now().date())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
