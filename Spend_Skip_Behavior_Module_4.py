def age_salary_employees():
    # opening both the files in reading modes
    with open("employees.txt") as f1:
        old_employees_high_sal = []
        old_employees_low_sal = []
        young_employees_high_sal = []
        young_employees_low_sal = []
        for i in f1.readline():
            employee_file = f1.readline()
            if employee_file.strip():
                # string to list which adds commas!
                employee_b = employee_file.split()
                person_info = int(employee_b[2])
                # salary and missed days employee
                sal_missed = list(employee_b[3:5])
                sal_missed = [int(element) for element in sal_missed]
                if sal_missed[0]<1000:
                    if sal_missed[0]>100:
                        sal_missed[0]=sal_missed[0]*10
                    if sal_missed[0]<100:
                        sal_missed[0] = sal_missed[0]*100
                if person_info <= 1970:
                    if sal_missed[0] >= 5000:
                        old_employees_high_sal.append(sal_missed)
                    else:
                        old_employees_low_sal.append(sal_missed)
                if person_info > 1970:
                    if sal_missed[0] >= 5000:
                        young_employees_high_sal.append(sal_missed)
                    else:
                        young_employees_low_sal.append(sal_missed)
    # days missed for employees
    count = 0
    total_days = 0
    for i in young_employees_low_sal:
        count = count + 1
        total_days = total_days + i[1]
    average_missed = total_days/count
    print("On average, younger employees with lower salaries missed:",average_missed, "days of work.")
    count = 0
    total_days = 0
    for i in young_employees_high_sal:
        count = count + 1
        total_days = total_days + i[1]
    average_missed = total_days / count
    print("On average, younger employees with higher salaries missed:", average_missed, "days of work.")
    count = 0
    total_days = 0
    for i in old_employees_high_sal:
        count = count + 1
        total_days = total_days + i[1]
    average_missed = total_days / count
    print("On average, older employees with higher salaries missed:", average_missed, "days of work.")

age_salary_employees()

def age_salary_customers():
    with open("customers.txt") as f2:
        old_customers_high_sal = []
        old_customers_low_sal = []
        young_customers_high_sal = []
        young_customers_low_sal = []
        for i in f2.readline():
            customer_file = f2.readline()
            if customer_file.strip():
                # string to list which adds commas!
                customer_b = customer_file.split()
                # employee tuple
                person_info = int(customer_b[2])
                tuplePerson = tuple(customer_b[0:3])
                # empty list for the employee information
                listLineA = []
                listLineA.append(tuplePerson)
                # purchases
                purchasesA = customer_b[3:4]
                listLineA.append(purchasesA)
                purchaseInfo = customer_b[4:]
                list_customer = []
                for i in purchaseInfo:
                    if '/' in purchaseInfo:
                        purchaseInfo.remove('/')
                for i in range(0, len(purchaseInfo) - 1, 2):
                    pair = [purchaseInfo[i], purchaseInfo[i + 1]]
                    list_customer.append(pair)
                purchasesA.append(list_customer)
                salary = int(listLineA[1][0])
                integer_list = [int(i) for j in list_customer for i in j]
                if person_info <= 1970:
                    if salary >= 5000:
                        old_customers_high_sal.append(integer_list)
                    else:
                        old_customers_low_sal.append(integer_list)
                if person_info > 1970:
                    if salary >= 5000:
                        young_customers_high_sal.append(integer_list)
                    else:
                        young_customers_low_sal.append(integer_list)
        flat_old_low = []
        i = 1
        for sublist in old_customers_low_sal:
                for val in sublist:
                    if i % 2 == 0:
                        flat_old_low.append(val)
                    i += 1
        sum_p = 0
        count = 0
        for i in flat_old_low:
            sum_p = sum_p + i
            count = count + 1
        average_spent = sum_p / count
        print("On average, older employees with lower salaries spent:", round(average_spent,2))
        flat_old_high = []
        i = 1
        for sublist in old_customers_high_sal:
            for val in sublist:
                if i % 2 == 0:
                    flat_old_high.append(val)
                i += 1
        sum_p = 0
        count = 0
        for i in flat_old_high:
            sum_p = sum_p + i
            count = count + 1
        average_spent = sum_p / count
        print("On average, older employees with higher salaries spent:", round(average_spent,2))
        flat_young_high = []
        i = 1
        for sublist in young_customers_high_sal:
            for val in sublist:
                if i % 2 == 0:
                    flat_young_high.append(val)
                i += 1
        sum_p = 0
        count = 0
        for i in flat_young_high:
            sum_p = sum_p + i
            count = count + 1
        average_spent = sum_p / count
        print("On average, younger employees with higher salaries spent:", round(average_spent,2))
        flat_young_low = []
        i = 1
        for sublist in young_customers_low_sal:
            for val in sublist:
                if i % 2 == 0:
                    flat_young_low.append(val)
                i += 1
        sum_p = 0
        count = 0
        for i in flat_young_low:
            sum_p = sum_p + i
            count = count + 1
        average_spent = sum_p / count
        print("On average, younger employees with lower salaries spent:", round(average_spent,2))

age_salary_customers()