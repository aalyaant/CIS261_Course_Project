#Alyce Gaines
#CSI261
#Course Project Phase 2

#Calculations
from datetime import datetime

FILENAME = "Employees.txt"

with open(FILENAME, "r") as employee_file:
    while True:
        rundate = input("Enter Report Start Date - MM/DD/YYYY or 'All':  ")
        if run_date.upper() == "All":
            break
        try:
            run_date = datetime.strptime(run_date, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid Date Format. Try Again.")
            break
        while True:
            employee_detail = employee_file.readline()
            if not employee_detail:
                break
            employee_detail = employee_detail.replace("\n", "")
            employee_list = employee_detail.split("|")


def get_employee_name():
    name = input("Enter Employee Name: ")
    return employee_name

def get_from_and_to_dates():
    while True:
        from_date = input("Enter From Date - Format:MM/DD/YYYY: ")
        try:
            from_date = datetime.strptime(from_date, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid Date Format. Try Again.")
        break
    while True:
        to_date = input("Enter To Date - Format:MM/DD/YYYY: ")
        try:
            to_date = datetime.strptime(to_date, "%m/%d/%Y").date()
        except ValueError:
            print("Invalid Date Format. Try Again.")
        if to_date <= from_date:
            print("To Date Must Cannot Precede From Date. Try Again.")
        else:
            break
    return from_date, to_date

def get_hourly_rate():
    hourly_rate = float(input("Enter Hourly Wage: "))
    return hourly_rate

def get_total_hours():
    total_hours = float(input("Enter Total Hours: "))
    return total_hours

def get_tax_rate():
    tax_rate = float(input("Enter Tax Rate: "))
    return tax_rate

def get_gross_pay(hourly_rate, total_hours):
    gross_pay = float(hourly_rate) * float(total_hours)
    return gross_pay

def print_info(details_printed):
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00

def calculate_tax_and_net_pay(hourly_rate, total_hours, tax_rate):
    gross_pay = float(hourly_rate) * float(total_hours)
    tax_rate = (float(tax_rate) / 100)
    net_pay = float(hourly_rate) * float(total_hours) - float(tax_rate)
    return tax_rate, net_pay

def display_employee_info(name, from_date, to_date, hourly_rate, total_hours, gross_pay, tax_rate, net_pay):
    print("Employee Name:", name)
    print("From Date:", from_date.strftime('%m/%d/%Y'))
    print("To Date:", to_date.strftime('%m/%d/%Y'))
    print("Hourly Rate:", hourly_rate)
    print("Total Hours:", total_hours)
    print("Gross Pay:", gross_pay)
    print("Tax Rate:", tax_rate)
    print("Net Pay:", net_pay)

def calculate_employees_taxes(employee_list, total_dict):
    for employee in employee_list:
        name, from_date, to_date, hourly_rate, total_hours = employee
        gross_pay = get_gross_pay(hourly_rate, total_hours)
        tax_rate, net_pay = calculate_tax_and_net_pay(hourly_rate, total_hours, tax_rate)
        display_employee_info(name, from_date, to_date, hourly_rate, total_hours)
        total_dict['total_employees'] += 1
        total_dict['total_hours'] += total_hours
        total_dict['total_gross_pay'] += gross_pay
        total_dict['total_tax'] += tax_rate
        total_dict['total_net_pay'] += net_pay

def display_total_info(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("Total Number of Employees:", total_dict['total_employees'])
    print("Total Hours:", total_dict['total_hours'])
    print("Total Gross Pay:", total_dict['total_gross_pay'])
    print("Total Tax:", total_dict['total_tax'])
    print("Total Net Pay:", total_dict['total_net_pay'])

def print_totals(employee_totals):
    print(f"Total Number of Employees: {employee_totals["total_employees"]}")
    print(f"Total Hours: {employee_totals["total_hours"]: ,.2f}")
    print(f"Total Gross Pay: {employee_totalss["total_gross_pay"]: ,.2f}")
    print(f"Total Tax:  {employee_totals["total_tax_rate"]: ,.2f}")
    print(f"Total Net Pay: {employee_totals["total_net_pay"]: ,.2}")

def main():
    employee_list = []
    total_dict = {"total_employees" : 0, " total_hours" : 0, "total_gross_pay" : 0, "total_tax_rate" : 0, "total_net_pay" : 0}

    while True:
        name = get_employee_name()
        if name == "End":
            break
        from_date, to_date = get_from_and_to_dates()
        hourly_rate = get_hourly_rate()
        total_hours = get_total_hours()
        tax_rate = get_tax_rate()
        employee_list.append([name, from_date, to_date, hourly_rate, total_hours, tax_rate])
        calculate_employees_taxes(employee_list, total_dict)
        display_total_info(total_dict)


if __name__ == "__main__":
    with open(FILENAME, "a") as employee_file:
        employee_detail_list = []
        employee_totals = {}
        details_printed = False
        while True:
            employee_name = get_employee_name()
            if employee_name.upper() == "End":
                break
            employee_detail = from_date + "|" + to_date + "|" +  employee_name + "|" + str(Hourly_rate) + "|" + str(total_hours)  + "|" + str(tax_rate) + "\n"
            employee_file.write(employee_detail)

        employee_file.close()
        printinfo(details_printed)