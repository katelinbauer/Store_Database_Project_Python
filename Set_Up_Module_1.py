# employee information data file = f1
# customer information data file = f2

def database_people():
    with open("employees.txt") as f1, open("customers.txt") as f2:
        # reading employee data file contents:
        for i in f1.readline():
            employee_file = f1.readline()
            if employee_file.strip():
                employee_b = employee_file.split()
                # employee information tuple
                person_e = tuple(employee_b[0:3])
                # salary and missed days
                sal_missed = list(employee_b[3:5])
                employee = "employee"
                # empty list to store employee information
                list_employee = []
                list_employee.append(person_e)
                list_employee.append(employee)
                list_employee.append(sal_missed)
                print(list_employee)
        # reading customer data file contents:
        for i in f2.readline():
            customer_file = f2.readline()
            if customer_file.strip():
                customer_b = customer_file.split()
                # customer information tuple
                person_c = tuple(customer_b[0:3])
                customer = "customer"
                # empty list to store customer information
                list_customer = []
                list_customer.append(person_c)
                list_customer.append(customer)
                # customer purchases
                purchases = customer_b[3:4]
                list_customer.append(purchases)
                purchase_info = customer_b[4:]
                list_customer_clean = []
                for i in purchase_info:
                    if '/' in purchase_info:
                        purchase_info.remove('/')
                for i in range(0, len(purchase_info)-1,2):
                    pair = [purchase_info[i], purchase_info[i + 1]]
                    list_customer_clean.append(pair)
                purchases.append(list_customer_clean)
                print(list_customer)


def database_purchases():
    # reading customer data file contents:
    with open("customers.txt") as f2:
        database = {}
        for i in f2.readline():
            customer_file = f2.readline()
            if customer_file.strip():
                customer_b = customer_file.split()
                customer_b[1] = int(customer_b[1])
                # customer information tuple
                person_c = tuple(customer_b[0:3])
                # empty list for the customer information
                list_customer = [person_c]
                # customer purchases
                purchases = customer_b[3:4]
                list_customer.append(purchases)
                purchase_info = customer_b[4:]
                # store customer purchases in list:
                list_customer_clean = []
                for i in purchase_info:
                    if '/' in purchase_info:
                        purchase_info.remove('/')
                for i in range(0, len(purchase_info) - 1, 2):
                    pair = [purchase_info[i], purchase_info[i + 1]]
                    list_customer_clean.append(pair)
                purchases.append(list_customer_clean)
                dict_my = {person_c[1]: purchases[1:]}
                database.update(dict_my)
        return(database)


print(database_purchases())
