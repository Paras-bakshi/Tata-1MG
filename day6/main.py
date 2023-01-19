class bank_account:
  __count_withdrawal=0
  __count_deposits=0
  __amount_five_deposits=0
  __deposit_log=[]
  __withdraw_log=[]

  def setter_amount(self,amount=0):
      self.__amount=self.__amount+amount
  def getter_amount(self):
      return self.__amount

  def setter_count_withdrawal(self):
      self.__count_withdrawal=self.__count_withdrawal+1
  def getter_count_withdrawal(self):
      return self.__count_withdrawal

  def setter_count_deposits(self):
      self.__count_deposits=self.__count_deposits+1
  def getter_count_deposits(self):
      return self.__count_deposits

  def setter_amount_five_deposits(self):
      self.__amount_five_deposits=self.__amount_five_deposits+1
  def getter_amount_five_deposits(self):
      return self.__amount_five_deposits

  def setter_deposit_log(self,amount):
      self.__deposit_log.append(amount)
  def getter_depoit_log(self):
      return self.__deposit_log

  def setter_withdraw_log(self,amount):
      self.__withdraw_log.append(amount)
  def getter_withdraw_log(self):
      return self.__withdraw_log

# Taking zero as a default value of initialize
  def __init__(self, amount=0):
    print("Account initialized by amount = ", amount)
    self.__amount = amount

# Create deposit and withdraw methods
  def deposit(self,amount_deposit):
      self.__amount=self.__amount+amount_deposit
      self.__count_deposits=self.__count_deposits+1
      self.__amount_five_deposits=self.__amount_five_deposits+amount_deposit
      print("Amount Deposited ",amount_deposit)
      print("Total Amount after Deposit ",self.__amount)
      self.__deposit_log.append(amount_deposit)
      if(len(self.__deposit_log)==11):
          del self.__deposit_log[0]

      if(self.__count_deposits==5):
          self.__count_deposits=0
          print("Due to 5 deposit count charges = ",0.01*(self.__amount_five_deposits))
          print("Total Balance = ",self.__amount-0.01*(self.__amount_five_deposits))
          self.__amount=self.__amount-0.01*(self.__amount_five_deposits)
          self.__amount_five_deposits=0

# Created a deposit_log method which will print the last 10 deposit amounts in the account.
  def deposit_log_method(self):
      print("Deposited logs = ",self.__deposit_log)

  def withdraw(self,amount_withdraw):
      if(amount_withdraw>self.__amount):
          print("Amount exceed balance not available")
      else:
          self.__amount=self.__amount-amount_withdraw
          print("Amount Withdraw ", amount_withdraw)
          print("Total Amount after Withdraw ", self.__amount)
          self.__count_withdrawal=self.__count_withdrawal+1
          if(self.__count_withdrawal==3):
              self.__amount=self.__amount-10
              print("Total Balance after withdraw charge of 3 times deduction =",self.__amount-10)
          self.__count_withdrawal=0
          self.__withdraw_log.append(amount_withdraw)
          if (len(self.__withdraw_log) == 11):
              del self.__withdraw_log[0]

# Create a withdraw_log method for the last 10 withdrawal amounts from the account.
  def withdraw_log_method(self):
      print("Withdraw logs = ",self.__withdraw_log)

# Create a method which will print the remaining balance of the bank account.
  def remaining_balance(self):
      print("The remaining balance = ",self.__amount)


# Inherited child class
class savings_account(bank_account):
    def __init__(self,amount=0):
        super().__init__(amount)

# Create deposit and withdraw methods
    def deposit(self, amount_deposit):

        self.setter_amount(amount_deposit)
        self.setter_count_deposits()
        print("Amount Deposited ", amount_deposit)
        print("Total Amount after Deposit ", self.getter_amount())
        self.setter_amount_five_deposits()
        self.setter_deposit_log(amount_deposit)
        if (len(self.getter_depoit_log()) == 11):
              del self.getter_depoit_log()[0]

        if (self.getter_count_deposits() == 5):
            self.setter_count_deposits(0)
            self.setter_amount(self.getter_amount()- 0.005 *(self.getter_amount_five_deposits()))
            self.setter_amount_five_deposits(0)

    def withdraw(self, amount_withdraw):
        if (amount_withdraw > self.getter_amount()):
            print("Amount exceed balance not available")
        else:
            self.setter_amount(-amount_withdraw)
            print("Amount Withdraw ",amount_withdraw)
            print("Total Amount after Withdraw ",self.getter_amount())
            self.setter_count_withdrawal()
            if (self.getter_count_withdrawal() == 3):
                self.setter_amount(self.getter_amount()-5)
            self.setter_count_withdrawal()
            self.setter_withdraw_log(amount_withdraw)
            if (len(self.getter_withdraw_log()) == 11):
                del self.getter_withdraw_log()[0]

p1 = bank_account(1000)
p1.deposit(1000)
p1.withdraw(500)
p1.withdraw_log_method()
p1.deposit_log_method()
p1.remaining_balance()

p2=savings_account(2000)
p2.deposit(1000)
p2.withdraw(500)
p2.withdraw_log_method()
p2.deposit_log_method()
p2.remaining_balance()
