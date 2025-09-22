#Alyce Gaines
#CSI261
#Course Project Phase 2

#Calculations
import datetime

def calculate_tax_and_net_pay(hourly_rate, total_hours, tax_rate):
    gross_pay = float(hourly_rate) * float(total_hours)
    tax_rate = (float(tax_rate) / 100)
    net_pay = float(hourly_rate) * float(total_hours) - float(tax_rate)
    return tax_rate, net_pay

def get_name():
    name = input("Enter Employee Name: ")
    return name

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

#Info
def get_from_and_to_dates():
    from_date = input("Enter From Date - Format:MM/DD/YYYY:")
    from_date = datetime.datetime.strptime(from_date,"%m/%d/%Y").date()
    to_date = input("Enter To Date - Format:MM/DD/YYYY:")
    to_date = datetime.datetime.strptime(to_date,"%m/%d/%Y").date()
    return from_date, to_date

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
    print("________________________________________________________________")
    print("Total Number of Employees:", total_dict['total_employees'])
    print("Total Hours:", total_dict['total_hours'])
    print("Total Gross Pay:", total_dict['total_gross_pay'])
    print("Total Tax:", total_dict['total_tax'])
    print("Total Net Pay:", total_dict['total_net_pay'])
    print("________________________________________________________________")

def main():
    employee_list = []
    total_dict = {"total_employees" : 0, " total_hours" : 0, "total_gross_pay" : 0, "total_tax_rate" : 0, "total_net_pay" : 0}

    while True:
        name = get_name()
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
    main()