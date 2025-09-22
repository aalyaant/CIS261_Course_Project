#Alyce Gaines
#CSI261
#Course Project Phase 1

#Calculations
def calculate_tax_and_net_pay(hourly_rate, total_hours, tax_rate):
    gross_pay = float(hourly_rate) * float(total_hours) * float(tax_rate)
    tax_rate = (float() / 100)
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

def get_gross_pay(hourly_rate, total_hours, tax_rate):
    gross_pay = float(hourly_rate) * float(total_hours) * float(tax_rate)
    return gross_pay

def get_tax_rate():
    tax_rate = float(input("Enter Tax Rate: "))
    return tax_rate

#Info
def display_employee_info(name, hourly_rate, total_hours, gross_pay, tax_rate, net_pay):
    print("________________________________________________________________")
    print("Employee Name:", name)
    print("Hourly Rate:", hourly_rate)
    print("Total Hours:", total_hours)
    print("Gross Pay:", gross_pay)
    print("Tax Rate:", tax_rate)
    print("Net Pay:", net_pay)
    print("________________________________________________________________")

def display_total_info(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print("________________________________________________________________")
    print("Total Number of Employees:", total_employees)
    print("Total Hours:", total_hours)
    print("Total Gross Pay:", total_gross_pay)
    print("Total Tax:", total_tax)
    print("Total Net Pay:", total_net_pay)
    print("________________________________________________________________")

def main():
    #Keep Total Counts
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_net_pay = 0

    while True:
        name = get_name()
        if name == "End":
            break
        hourly_rate = get_hourly_rate()
        hours = get_total_hours()
        tax_rate = get_tax_rate()
        gross_pay = get_gross_pay(hourly_rate, hours, tax_rate)
        tax_rate, net_pay = calculate_tax_and_net_pay(hourly_rate, hours, tax_rate)

        display_employee_info(name, hourly_rate, hours, gross_pay, tax_rate, net_pay)

        #Update Total Counts
        total_employees += 1
        total_hours += hours
        total_gross_pay += net_pay
        total_tax += tax_rate
        total_net_pay += net_pay

        display_total_info(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)


if __name__ == "__main__":
    main()