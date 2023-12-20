def greatest_skip():
    with open("employees.txt") as f1, open("customers.txt") as f2:
        missed_days = []
        all_employees = []
        for i in f1.readline():
            employee_file = f1.readline()
            if employee_file.strip():
                employee_b = employee_file.split()
                # employee information
                sal_missed = list(employee_b[3:5])
                days = sal_missed[1]
                missed_days.append(int(days))
                all_employees.append(employee_b)
            max_val = max(missed_days)
        index = missed_days.index(max_val)
        skipper = all_employees[index][0]
        skipped_num = all_employees[index][4]
        print("The greatest work skipper is", skipper, "who missed", skipped_num,"days of work!")

def greatest_spend():
 with open("customers.txt") as f2:
    all_customers = []
    people = []
    for i in f2.readline():
        customer_file = f2.readline()
        if customer_file.strip():
            customer_b = customer_file.split()
            person_c = tuple(customer_b[0:3])
            people.append(person_c)
            # purchases made by customers
            purchase_info = customer_b[4:]
            list_customer = []
            for i in purchase_info:
                if '/' in purchase_info:
                    purchase_info.remove('/')
            for i in range(0, len(purchase_info) - 1, 2):
                pair = [int(purchase_info[i]), int(purchase_info[i + 1])]
                list_customer.append(pair)
            all_customers.append(list_customer)
    all_the_totals = []
    for sublist in all_customers:
        sum_total = 0
        for inner_sublist in sublist:
            second_element = inner_sublist[1]
            sum_total = second_element + sum_total
        all_the_totals.append(sum_total)
    max_spend = max(all_the_totals)
    index = all_the_totals.index(max_spend)
    spender = people[index][0]
    print("The greatest spender is", spender, "who spent $", max_spend)

greatest_spend()

greatest_skip()

