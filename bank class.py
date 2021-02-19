class Bank:
  def __init__(self):
      self.balance=0
self.accountno=int(input("enter account number:"))
self.name=input("enter name:")
self.accounttype=input("enter account type.")
def display(self):
      print("name:",self.name)
      print("Accountnumber",self.accountno)
      print("Accounttype:",self.accounttype)
      def deposite(self):
          amount=int(input("enter the account to deposite:"))
          self.balance+=amount
          print("your balance is",self.balance)
          def withdraw(self):
              amount=int(input("enter the amount to withdraw:"))
          if(amount>self.balance):
                     print("insufficient balance")
          else:
                        self.balance=amount
                        print("your remaining balance is:",self.balance)
account=Bank()
account.display()
account.deposit()
account.withdraw()
