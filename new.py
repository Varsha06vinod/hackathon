name= str(input("Enter name of employee:"))
ctc=float(input("Enter CTC :"))
basic_salary=ctc*50/100
da=float(basic_salary*0.25)
hra=float(basic_salary*0.15)
pf=float((basic_salary+da)*0.12)
ta=float(basic_salary*0.075)
netpay=float(basic_salary+da+hra+ta)
grosspay=float(netpay-pf)
print("name of employee:",name)
print("CTC:",ctc)
print("Basic salary:",basic_salary)
print("dearness allowance:",da)
print("House rent allowance:",hra)
print("name of travel:",ta)
print("name of netpay:",netpay)
print("name of grosspay:",grosspay)







