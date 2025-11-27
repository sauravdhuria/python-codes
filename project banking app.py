balance=0.0
kyc_document={}
def checking_balance():
    print(f"your balance is :{balance}")
    print("==========================")
def deposit(amount):
    global balance
    if amount<=0:
        print("Cannot deposit negative or zero amount")
        print("==========================")
    else:
        balance+=amount
        print(f"{amt} deposited successfully")
        print("==========================")
        print(f"your balance is {balance}")
        print("==========================")

def withdraw(amount):
    global balance
    if amount<0 :
        print("cannot withdraw negative amount ")
        print("==========================")
    elif amount>balance:
        print("insufficient balance")
        print("==========================")
    else:
        balance-=amount
        print(f"{amount} withdred successfully")
        print(f"your balance is {balance}")
        print("==========================")

def update_kyc(docs):
    global kyc_document
    kyc_document.update(docs)

def check_kyc(**docs):
    global kyc_document
    if len(kyc_document) == 0:
        print("==========================")
        print("kyc not done")
        print("==========================")

    else:
    for doc in kyc_document:
        print("==========================")
        print(f"{doc} : {kyc_document[doc]}")
if __name__=="__main__":
    while True:
        print("===================")
        print("welcome to the bank")
        print("===================")
        print()
        print("1.  check balance")
        print("2.  deposit")
        print("3.  withdraw")
        print("4.  update kyc")
        print("5.  check kyc")

        print("6.  exit")

        choice=input("enter your choice:")
        print("==========================")
        if choice=="1":
            checking_balance()

        elif choice=="2":
            amt=float(input("Enter your amount to be deposited:"))
            deposit(amt)
        elif choice=="3":
            amt=float(input("Enter your amount to be withdraw:"))
            withdraw(amt)
        elif choice=="4":
            kyc_docs={}
            n_document=int(input("enter your number of document you want to add:"))
            for i in range(n_document):
                key=input("enter the document type :")
                value=input("enter the document number :")
                kyc_docs[key]=value
            update_kyc(kyc_docs)
            print("kyc updated")
        elif choice=="5":
            check_kyc()
        elif choice=="6":
            print()
            print("Thankyou for banking with us")
            break
        else:
            print("enter valid choice")




