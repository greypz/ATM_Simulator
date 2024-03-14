class Account:
    def __init__(self, isim, password ,soyisim="unknown",phone_number="unknown", account_balance=0,):
        self.isim = isim
        self.soyisim = soyisim
        self.tel_no = phone_number
        self.başlangıç_parası = account_balance
        self.password = password
    def paraAktarimi(self,targetaccount):
        designated_amount=int(input("How much do you want to transfer? "))
        if designated_amount > self.başlangıç_parası:
            print("\nYou dont have enough AmongCOIN for that you lil poor nigga")
        else:
            self.başlangıç_parası = self.başlangıç_parası - designated_amount
            targetaccount.başlangıç_parası+=designated_amount

        
    def paraCekimi(self):
        cekimMiktarı = int(input("Withdraw: "))
        if self.cekimMiktarı > self.başlangıç_parası:
            print("\nYou dont have enough AmongCOIN for that you lil poor nigga")
        else:
            self.başlangıç_parası = self.başlangıç_parası - cekimMiktarı

    def bilgi(self):
        print("Mr.",self.isim, self.soyisim)
        print("Phone Number:",self.tel_no)
        print("Account Balance:",self.başlangıç_parası,"ඞ")
    def paraYatirimi(self):
        self.başlangıç_parası = self.başlangıç_parası + int(input("Deposit: "))

    def balanceinfo(self):
        print("Account Balance:",self.başlangıç_parası,"ඞ")

##deneme