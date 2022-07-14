

def incometax(income):

    if not isinstance(income,float):
        print("please input with decimal")


    incomeRange = [20,10,10,40,40,40,40,40,40,40,180,500]
    taxRange = [0,2,3.5,7,11.5,15,18,19,19.5,20,22,23]

    income /= 1000
    taxableIncome = 0
    for i in range(len(incomeRange)):
        if income - incomeRange[i] <= 0: 
            taxableIncome += income * (taxRange[i]/100)
            return taxableIncome*1000
        elif income - incomeRange[i] > 0:
            taxableIncome += incomeRange[i] * (taxRange[i]/100) if incomeRange[i] - income < 0 else (income-incomeRange[i]) * (taxRange[i]/100)
            income = income - incomeRange[i]
    return taxableIncome*1000

taxableIncome = incometax(67200.00)

print (taxableIncome)

            

