class Account:
    def __init__(self, isim, password, soyisim="unknown", phone_number="unknown", account_balance=0, ):
        self.isim = isim
        self.soyisim = soyisim
        self.tel_no = phone_number
        self.başlangıç_parası = account_balance
        self.password = password

    def paraAktarimi(self, targetaccount,designated_amount):
        if designated_amount > self.başlangıç_parası:
           return False
        else:
            self.başlangıç_parası = self.başlangıç_parası - designated_amount
            targetaccount.başlangıç_parası += designated_amount
            return True

    def paraCekimi(self,cekimMiktarı):
        if cekimMiktarı > self.başlangıç_parası:
            return False
        else:
            self.başlangıç_parası = self.başlangıç_parası - cekimMiktarı
            return True

    def bilgi(self):
        print("Mr.", self.isim, self.soyisim)
        print("Phone Number:", self.tel_no)
        print("Account Balance:", self.başlangıç_parası, "ඞ")

    def paraYatirimi(self,deposit_amount):
        self.başlangıç_parası = self.başlangıç_parası + deposit_amount

    def balanceinfo(self):
        print("Account Balance:", self.başlangıç_parası, "ඞ")

