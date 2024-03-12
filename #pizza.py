#pizza
size=input("size of your pizza:")
bill=0
if size=='s':
    bill=100
    print(f"pay {bill}")
elif size=='m':
    bill=200
    print(f"pay {bill}")
elif size=='l':
    bill=300
    print(f"pay {bill}")
cheese=input("do you want cheese")
if cheese=='y':
    bill=bill+50
    print(f"your total is {bill}")
pep=input("do you want peparoni")
if size=='s':
    if pep=='y':
        bill=bill+30
        print(f"your total is {bill}")
if size=='m' or 'l':
    if pep=='y':
        bill=bill+50
        print(f"your total is {bill}")
