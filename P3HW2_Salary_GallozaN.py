#CTI 110
#P3HW2 Salary
#Natasha Galloza
#11/10/2024

employee_name = input("Enter employee's name: ")
work_hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print ("-" * 30)

print("Employee name: ", employee_name)
print("")

print("Hours Worked    Pay Rate    OverTime    OverTimePay    RegHour Pay    Gross Pay    ")
print ("-" * 90)

#Setting the hours
reg_hours = min(work_hours, 40)
over_hours = max(0, work_hours - 40)

#OverTime
over_time = float('5.0')
over_pay = int(over_hours) * int(pay_rate * over_time)

#Regular
reg_pay = int(work_hours) * int(pay_rate)
gross_pay = int(reg_pay) + int(over_pay)

print(f'{work_hours:<16}{pay_rate:<12.2f}{over_time:<12.2f}{over_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:.2f}')
