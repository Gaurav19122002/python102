#multiple if statments
age=int(input("enter your"))
if age<12:
    print("pay 250$")
    bill=250
elif age<18:
    print("pay 300$")
    bill=300
elif age<=18:
    print("pay 500$")
    bill=500
want_photo = input("do you want photo? Y/N")
if want_photo== 'y':
    bill=bill+50
    print(f"pay {bill}$")