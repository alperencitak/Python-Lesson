accounts = {
    1693:{
    "name": "Jacob",
    "surname": "Swartz",
    "balance": 150000
},
1385:{
    "name": "Elena",
    "surname": "Raus",
    "balance": 485000
}}
while True:
    giris = 0
    enterCode = int(input("Please enter the your account code : "))
    for kontrol in accounts:
        if enterCode == kontrol:
            giris = 1
    if giris == 1:break
    else:print("Wrong Code! Try Again...")
print(f"---Account Info---",
      f"Name: {accounts[enterCode]["name"]}",
      f"Surname: {accounts[enterCode]["surname"]}",
      f"Balance: {accounts[enterCode]["balance"]}",sep="\n")
print("\n1 - Withdraw\n2 - Deposit")
islem = int(input("\nEnter the action number : "))
def withdraw(AmountF):
    accounts[enterCode]["balance"] -= AmountF
def deposit(AmountF):
    accounts[enterCode]["balance"] += AmountF

if islem==1:
    while True:
        Amount = int(input("\nEnter the amount : "))
        if Amount<=accounts[enterCode]["balance"]:break
        else:print("Not enought money! Try Again")
    withdraw(Amount)
if islem==2:
    Amount = int(input("\nEnter the amount : "))
    deposit(Amount)
print(f"---Account Info---",
      f"Name: {accounts[enterCode]["name"]}",
      f"Surname: {accounts[enterCode]["surname"]}",
      f"Balance: {accounts[enterCode]["balance"]}",sep="\n")
