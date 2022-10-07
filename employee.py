"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class commission():
    commission_type = ''
    commission_string = ''

    def __init__(self, type, *args):
        if(type == 'C'):
            self.commission_string = " and receives a commission for " + str(args[0]) + " contract(s) at " + str(args[1]) + "/contract"
        elif(type == 'B'):
            self.commission_string = " and receives a bonus commission of " + str(args[0])

    def get_commission_str(self):
        return self.commission_string

class contract():
    contract_type = ''
    contract_string = ''

    def __init__(self,type,*args):
        if(type == 'C'):
            self.contract_string = " works on a monthly salary of " + str(args[0])
        elif(type == 'H'):
            self.contract_string = " works on a contract of " +  str(args[0]) + " hours at " +  str(args[1]) + "/hour"

    def get_contract_str(self):
        return self.contract_string
class Employee:

    def __init__(self,emp_name,contract,commission):
        self.name = emp_name
        self.emp_contract = contract
        self.emp_commission= commission
        self.total_pay = 0




    def __str__(self):
        output_str = self.name

        if(self.emp_commission is None):
            output_str += self.emp_contract
        else:
            output_str += self.emp_contract + self.emp_commission

        output_str += "." + " Their total pay is " + str(self.total_pay) + "."

        return output_str

    def get_pay(self):
        return self.total_pay

    def set_contract(self,monthly):
        self.total_pay += monthly

    def set_hourly(self,hours,per_hour):
        self.total_pay += (hours * per_hour)

    def set_commission_bonus(self,bonus):
        self.total_pay += bonus

    def set_commission_contracts(self,contract_num, rate_per_contract):
        self.total_pay += (contract_num * rate_per_contract)

# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie_contract = contract('C',4000)
billie_commision = commission(None)
billie = Employee('Billie',billie_contract.get_contract_str(),billie_commision.get_commission_str())
billie.set_contract(4000)


# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie_contract = contract('H',100,25)
charlie_commision = commission(None)
charlie = Employee('Charlie',charlie_contract.get_contract_str(),charlie_commision.get_commission_str())
charlie.set_hourly(100,25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract = contract('C',3000)
renee_commision = commission('C',4,200)
renee = Employee('Renee',renee_contract.get_contract_str(), renee_commision.get_commission_str())
renee.set_contract(3000)
renee.set_commission_contracts(4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract = contract('H',150,25)
jan_commision = commission('C',3,220)
jan = Employee('Jan',jan_contract.get_contract_str(), jan_commision.get_commission_str())
jan.set_hourly(150,25)
jan.set_commission_contracts(3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_contract = contract('C',2000)
robbie_commision = commission('B',1500)
robbie = Employee('Robbie',robbie_contract.get_contract_str(), robbie_commision.get_commission_str())
robbie.set_contract(2000)
robbie.set_commission_bonus(1500)
print(robbie)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_contract = contract('H',120,30)
ariel_commision = commission('B',600)
ariel = Employee('Ariel',ariel_contract.get_contract_str(), ariel_commision.get_commission_str())
ariel.set_hourly(120,30)
ariel.set_commission_bonus(600)
print(ariel)
