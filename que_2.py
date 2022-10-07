
def percentage_to_value(percent ,basic_pay):
    return round((percent/100) * basic_pay)


def salary_details():
    basic_pay = float(input("Enter your basic pay: "))
    employee_id = input("Enter your employee id: ")
    employee_name = input("Enter your name: ")
    da = 0
    hra = 0
    net_pay = 0
    find_netpay = lambda basic_pay, da, hra: float(basic_pay) + float(da)+ float(hra)
    
    if basic_pay >= 10000:
        da += percentage_to_value(8.0, basic_pay)
        hra += percentage_to_value(15.0, basic_pay)
        net_pay += find_netpay(basic_pay, da, hra)

    elif basic_pay >= 5000 and basic_pay < 10000:
        da += percentage_to_value(5.0, basic_pay)
        hra += percentage_to_value(10.0, basic_pay)
        net_pay += find_netpay(basic_pay, da, hra)

    else:
        da += percentage_to_value(5.0, basic_pay)
        hra += percentage_to_value(3.0, basic_pay)
        net_pay += find_netpay(basic_pay, da, hra)

    print(f"Net pay, HRA, DA for employee id {employee_id} {employee_name} is: {net_pay}, {hra}, {da}")
    return (da, hra, net_pay)

if __name__ == "__main__":
    salary_details()


