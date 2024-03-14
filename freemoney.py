from account import Account
import json


with open("database.json",'r') as json_file:
    Accounts = json.load(json_file)

currentaccount=0

while currentaccount==0:
    givenpass= input("Welcome to amogus ATM's!, Enter your password: ")
    for account in Accounts:
        if givenpass == account['properties']['password']:
            print(account)
            currentaccount=Account(account['properties']['isim'],account['properties']['password'],account['properties']['soyisim'],account['properties']['tel_no'],account['properties']['baslangic_parasi'])
            break

    if currentaccount==0:
        print("\nYou need a password lil nigga\n")

while True:
        desicion= int(input("\n1 = Withdraw, 2 = Deposit, 3 = Transfer, 4 = Info, 5 = Exit, What you want? ",))
        if desicion == 1:
            currentaccount.paraCekimi()
            currentaccount.balanceinfo()
        elif desicion == 2:
            currentaccount.paraYatirimi()
            currentaccount.balanceinfo()
        elif desicion == 3:
            ownername=input('Enter the name of the account owner: ')
            for account in Accounts:
                if account['properties']['isim']==ownername:
                    targetaccount = Account(account['properties']['isim'], account['properties']['password'],
                                            account['properties']['soyisim'], account['properties']['tel_no'],
                                            account['properties']['baslangic_parasi'])
                    currentaccount.paraAktarimi(targetaccount)
                    currentaccount.balanceinfo()
        elif desicion == 4:
            currentaccount.bilgi()
        elif desicion == 5:
            print("\nThank you for choosing Amongese international bank, have a sussy day!")
            break

with open('database.json','w') as json_file:
    for account in Accounts:
        if account['properties']['isim']==currentaccount.isim:
            account['properties']["baslangic_parasi"]=currentaccount.başlangıç_parası
            break

    json.dump(Accounts,json_file,indent=2)