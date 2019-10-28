import sys
import string
punc = string.punctuation
detail = {}
bal=0
####################################################
def front():
    print('''\nChoices:
1. Signup
2. Login
3. Exit''')
    fch = int(input("Enter your choice: "))
    if fch==1:
        return signup()
    elif fch==2:
        return login()
    elif fch==3:
        print("Thankyou for Banking with us")
        sys.exit()
    else:
        print("Wrong Choice")
        sys.exit()
#####################################################
def signup():
    print("\nWelcome to Signup window")
    u_name = input("Create username: ")
    if u_name in detail.keys():
        print("Try entering different Username")
        front()
    while True:
        u_pwd = input("Create password: ")
        c=0
        if len(u_pwd)>5:
            for i in u_pwd:
                if i in punc:
                    detail[u_name] = u_pwd
                    front()
        else:
            print("Improper password, Read Guidelines")
#####################################################    
def login():
    print("\nWelcome to login window")
    global name
    name = input("Enter username: ")
    if name in detail.keys():
        attempt =3
        c_attempt =1
        while(c_attempt<=attempt):
            pwd = input("Enter password: ")
            if pwd == detail[name]:
                print(f"\nWelcome {name}, Login Successful")
                return service()
            else:
                print("Wrong Password")
                if (c_attempt==3):
                    print('Account Locked')
                    sys.exit()
                print(f'Attempts left {3-c_attempt}')
            c_attempt += 1
    else:
        print("Unknown User")
        sys.exit()
#####################################################
def service():
    print('''\nWelcome to banking services window
1. Balance Enquiry
2. Deposit
3. Withdraw
4. Change Password
5. Exit''')
    och = int(input("Enter your choice: "))
    if och==1:
        balance()
    elif och==2:
        cr = float(input("Enter deposit amount: "))
        deposit(cr)
    elif och==3:
        db = float(input("Enter withdrawl amount: "))
        withdraw(db)
    elif och==4:
        change_pwd()
    elif och==5:
        print("Thankyou for banking with us.")
        sys.exit()
    else:
        print("Unknown Input")
        sys.exit()
#####################################################        
def balance():
    print('Current balance is Rs.',bal)
    return service()
####################################################
def deposit(cd):
    global bal
    bal = bal+cd
    print('Now Balance is Rs.',bal)
    return service()
#####################################################
def withdraw(db):
    global bal
    if bal> db:
        bal = bal-db
        print('Now Balance is Rs.',bal)
    else:
        print('Insufficient balance')
    return service()
#####################################################
def change_pwd():
    new_pwd = input("Enter new password: ")
    detail[name]= new_pwd
    print("Password updated Successfully")
    return front()
#####################################################

print("Welcome to Python Bank")
front()



