"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum, unique

@unique
class commission(Enum):
    BONUS = str('B')
    CONTRACT_COMMISSION = str('C')

    def create_bonus_str(self,given_bonus):
        self.BONUS =  " and receives a bonus commission of " + given_bonus

    def create_contract_commission_str(self,contract_num,rate_per):
        self.CONTRACT_COMMISSION = " and receives a commission for " + contract_num + " contract(s) at " + rate_per + "/contract"

@unique
class contract(Enum):
    MONTHLY_CONTRACT = str('M')
    HOURLY = str('H')

    def create_contract_str(self, monthly):
        self.MONTHLY_CONTRACT = " works on a monthly salary of " + monthly

    def create_hourly_str(self,total_hrs,hourly):
        self.HOURLY = " works on a contract of" +  total_hrs + " hours at " +  hourly + "/hour"

class Employee:

    def __init__(self, name, pay, employee_contract, *hours):
        self.name = name
        self.wage = pay
        self.emp_contract = employee_contract
        self.total_pay = 0
        self.tot_hours = 0
        self.emp_commission = None

        if (len(hours) > 1):
            raise ValueError("Only one value for hourly rate can be entered")
            return

        if ((hours is not None) and (hours != ())):
            self.tot_hours = hours[0]
            print(self.tot_hours)

        if(employee_contract is contract.MONTHLY_CONTRACT):
            self.emp_contract.create_contract_str(self.wage)
            self.total_pay += self.wage
        else:
            self.emp_contract.create_hourly_str(self.tot_hours, self.wage)
            self.total_pay += (self.wage * self.tot_hours)

    def get_pay(self):
        return self.total_pay

    def __str__(self):
        output_str = ''
        output_str += self.name

        if(self.emp_contract is contract.HOURLY):
            output_str += self.emp_contract.HOURLY

        else:
            output_str += self.emp_contract.MONTHLY_CONTRACT

        if(self.emp_commission is not None):
            if(self.emp_commission is commission.BONUS):
                output_str += self.emp_commission.BONUS
            else:
                output_str += self.emp_commission.CONTRACT_COMMISSION

        output_str += "." + " Their total pay is " + self.total_pay
        return output_str

    def set_commission_bonus(self,bonus):
        self.emp_commission = commission.BONUS
        self.emp_commission.create_bonus_str(bonus)
        self.total_pay += bonus

    def set_commission_contracts(self,contract_num, rate_per_contract):
        self.emp_commission = commission.CONTRACT_COMMISSION
        self.emp_commission.create_contract_commission_str(contract_num,rate_per_contract)
        self.total_pay += (contract_num * rate_per_contract)

# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie',4000,contract.MONTHLY_CONTRACT)
print(billie)
# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie',25,contract.HOURLY,100)
print(charlie)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,contract.MONTHLY_CONTRACT)
renee.set_commission_contracts(4,200)
print(renee)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,contract.HOURLY,150)
jan.set_commission_contracts(3,220)
print(jan)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,contract.MONTHLY_CONTRACT)
robbie.set_commission_bonus(1500)
print(robbie)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,contract.HOURLY,120)
ariel.set_commission_bonus(600)
print(ariel)
