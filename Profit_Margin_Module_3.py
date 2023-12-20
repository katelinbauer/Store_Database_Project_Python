def B_R():
    # opening both the employee and the customer text files
    with open("employees.txt") as f1, open("customers.txt") as f2:
        import Set_Up_Module_1
        database_of_purchases = Set_Up_Module_1.database_purchases()
        purchases = list(database_of_purchases.values())
        flattened = []
        for sublist in purchases:
            for val in sublist:
                for val2 in val:
                    flattened.append(val2)
        purchases_item = []
        for inner in flattened:
            purchases_item.append(int(inner[1]))
        total_purchases_sum = sum(purchases_item)
        total_salary = 0
        for i in f1.readline():
            employee_file = f1.readline()
            if employee_file.strip():
                employee_b = employee_file.split()
                # employee information tuple
                person_e = tuple(employee_b[0:3])
                # salary and missed days
                sal_missed = list(employee_b[3:5])
                employee = "employee"
                # empty list for the employee information
                list_employee = []
                list_employee.append(person_e)
                list_employee.append(employee)
                list_employee.append(sal_missed)
                salary = int(list_employee[2][0])
                total_salary = total_salary + salary
        total_costs = total_salary + 2000
        r_b_value = total_costs - total_purchases_sum
        if total_purchases_sum > total_costs:
            print("the store is in the 'black' by $", r_b_value)
        else:
            print("The store is in the 'red' by $", r_b_value)

B_R()
