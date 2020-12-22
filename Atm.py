class Atm(object):
 def __init__(self,atmcardNo,atmcardPin):
  self.atmcardNo = atmcardNo
  self.atmcardPin = atmcardPin

 def CashWithdrawal(self):
  print("Cash Withdrawal Method")

 def BalanceEnquiry(self):
  print("BAlance Enquiry")


myCard = Atm(999999,1234)
myCard.CashWithdrawal()
myCard.BalanceEnquiry()