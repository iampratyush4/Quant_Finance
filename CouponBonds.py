class CouponBond:
    def __init__(self,principal,rate,maturity,interest_Rate):
        self.principal=principal
        self.rate=rate/100
        self.maturity=maturity
        self.interest_Rate=interest_Rate/100

    def present_val(self,x,n):
        return x/(1+self.interest_Rate)**n
    def calc_price(self):
        price=0
        for t in (1,self.maturity+1):
            price=price+ self.present_val(self.principal*self.rate,t)

        price=price+ self.present_val(self.principal,self.maturity)
        return price
if __name__=='__main__':
    bond=CouponBond(1000,10,3,4)
    print(bond.calc_price())