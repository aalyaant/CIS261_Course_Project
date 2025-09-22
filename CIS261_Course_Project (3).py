#Alyce Gaines
#CSI261
#Course Project Phase 2

from datetime import datetime
################################################################################
def login():
        # read login information and store in a list
    UserFile = open("Users.txt","r")
    UserList= []
    UserName = input("Enter User Name: ")
    UserRole = "None"
    while True:
       UserDetail = UserFile.readline()       
       if not UserDetail:
           return UserRole, UserName
       UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
       UserList = UserDetail.split("|")           
       if UserName == UserList[0]:
            UserRole = UserList[2] # user is valid, return role
            return UserRole, UserName
    return UserRole, UserName
################################################################################
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
            print("To Date Cannot Precede From Date. Try Again.")
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

def calculate_tax_and_net_pay(hourly_rate, total_hours, tax_rate):
    gross_pay = float(hourly_rate) * float(total_hours)
    tax_rate = (float(tax_rate) / 100)
    net_pay = float(hourly_rate) * float(total_hours) - float(tax_rate)
    return gross_pay, tax_rate, net_pay

def print_info(details_printed):
    total_employees = 0
    total_hours = 0.00
    total_gross_pay = 0.00
    total_tax = 0.00
    total_net_pay = 0.00

    employee_file = open(employees.txt, "r")
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
            from_date = employee_list[0]
            if (str(run_date).upper() != "All"):
                checkdate = datetime.strptime(from_date, "%m/%d/%Y")
                if (checkdate < run_date):
                    continue
            to_date = employee_list[1]
            employee_name = employee_list[2]
            hours = float(employee_list[3])
            hourly_rate = float(employee_list[4])
            tax_rate = float(employee_list[5])
            gross_pay, tax_rate, net_pay = calculate_tax_and_net_pay(hourly_rate, hours, tax_rate)
            print(employee_name, from_date, to_date, f"{hourly_rate: ,.2f}", f"{hours: ,.2f}", f"{gross_pay: ,.2f}", f"{tax_rate: ,.1%}", f"{net_pay: ,.2f}")

            total_employees['total_employees'] += 1
            total_hours['total_hours'] += total_hours
            total_gross_pay['total_gross_pay'] += gross_pay
            total_tax['total_tax'] += tax_rate
            total_net_pay['total_net_pay'] += net_pay
            employee_totals["total_employees"] = total_employees
            employee_totals["total_hours"] = total_hours
            employee_totals["total_gross_pay"] = total_gross_pay
            employee_totals["total_tax"] = total_tax
            employee_totals["total_net_pay"] = total_net_pay
            DetailsPrinted = True   
        if (DetailsPrinted):  #skip of no detail lines printed
            print_totals (employee_totals)
    else:
        print("no detail information to print")

def print_totals(employee_totals):    
    print(f'Total Number Of Employees: {employee_totals["TotEmp"]}')
    print(f'Total Hours: {employee_totals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {employee_totals["total_gross_pay"]:,.2f}')
    print(f'Total Tax:  {employee_totals["total_tax"]:,.2f}')
    print(f'Total Net Pay: {employee_totals["total_net_pay"]:,.2f}')

def create_users():
    print('##### create users, passwords, and roles #####')
    UserFile = open("Users.txt", "a+") 
    while True:
        username = get_user_name()
        if (username.upper() == "END"):
            break
        userpwd = get_user_password()
        userrole = get_user_role()

        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"  
        UserFile.write(UserDetail)
    # close file to save data
    UserFile.close()    
    get_printer_info()

def get_user_name():
    username = input("Enter user name or 'End' to quit: ")
    return username

def get_user_password():
    pwd = input("Enter password: ")
    return pwd

def get_user_role():
     userrole = input("Enter role (Admin or User): ")
     while True:       
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ") 

def get_printer_info():
    UserFile = open("Users.txt","r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)

############################################################################################

############################################################################################

if __name__ == "__main__":

    ##################################################

    create_users()
    print()
    print("##### Data Entry #####")
    UserRole, UserName = login() 
    DetailsPrinted = False  ###
    employee_totals = {} ###
    if (UserRole.upper() == "NONE"): #user not found in user file
        print(UserName," is invalid.")
    else:
    # only admin users can enter data
        if (UserRole.upper() == "ADMIN"):

            employee_file = open("Employees.txt", "a+")                
            while True:
                employee_name = get_employee_name()
                if (employee_name.upper() == "END"):
                    break
                from_date, to_date = get_from_and_to_dates()
                hours = get_hours()
                hourly_rate = get_hourly_rate()
                tax_rate = get_tax_rate()
                employee_detail = from_date + "|" + to_date  + "|" + employee_name  + "|" + str(hours)  + "|" + str(hourly_rate)  + "|" + str(tax_rate) + "\n"  
                employee_file.write(employee_detail)
        # close file to save data
            employee_file.close()    
        print_info(DetailsPrinted)