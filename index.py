class Spliter:
  def __init__(self, salary):
    self.salary = salary
  def needs(self):
    return self.salary*0.5
  def wants(self):
    return self.salary*0.3
  def savings(self):
    return self.salary*0.2
mode = (input("Crew or Slave:  ", )).upper()
if mode == "CREW" or mode == "SLAVE":
  if mode == "CREW":
    no_days = (float(input("Number of Days: ")))
    total_income = no_days*248.22
  if mode == "SLAVE":
    no_hours = (float(input("number of hours: ",)))
    total_income = no_hours*28.58
  

#  Deductions Culculator
  def deductions():
    UIF = total_income * 0.01
    Skills_Dev = total_income * 0.01
    despute_res = total_income * 0.001
    income_tax = 300
    total_deductions = UIF + Skills_Dev + despute_res + income_tax
    
    return total_deductions
    
  remaining_amount = total_income - deductions()
  
  Money = Spliter(remaining_amount)
  
  def debt_payment():
    bash = 325
    return  bash
  
  def monthly_expenses():
    funds_avail = round(Money.needs(), 2)
    debt = debt_payment()
    rent = 700
    total_m_e = debt + rent
    remain_m_e = funds_avail - total_m_e
    return total_m_e, remain_m_e, rent
  
  def ent_expanses():
    funds_avail = round(Money.wants(), 2)
    data = funds_avail*0.5 
    alcohol = funds_avail*0.3 
    remain_e_e = funds_avail*0.2
    return data, alcohol, remain_e_e
    
  def savings_goals():
    funds_avail = round(Money.savings(), 2)
    business_savings = funds_avail*0.5 
    emegancy_funds = funds_avail*0.3
    fixed_savings = funds_avail*0.2
    
    return business_savings, emegancy_funds, fixed_savings
  
  #---------- Print Statements ----------#
  
  # Calculating Income After Deductions
  
  print("----------------------------------")
  print("Total Income: R", round(total_income, 2))
  
  print("Total deductions: R", round(deductions(), 2))
  print("Remaining Amount: R", round(remaining_amount, 2))
  
  print("----------------------------------")
  
  # The 50/30/20 savings Calculations
  
  print("Needs: R", round(Money.needs(), 2))
  print("Wants: R", round(Money.wants(), 2))
  print("Savings: R", round(Money.savings(), 2))
  
  print("----------------------------------")
  
  # Culculating Needed Monthly Expenses #
  
  print("---------- Needs: ")
  print("Rent: ", (monthly_expenses()[2]))
  print("Total Debt: R", round(debt_payment(), 2) )
  print("Total Monthly Expenses: ",(monthly_expenses()[0]))
  print("Change: R", round(monthly_expenses()[1], 2))
  print("----------------------------------")
  
  # Calculating Wanted Monthly Expenses #
  
  print("---------- Wants: ")
  print("Data Cost: R", round(ent_expanses()[0], 2))
  print("Alcohol: ", round(ent_expanses()[1], 2))
  print("Change: R", round(ent_expanses()[2],2))
  
    # Savings Calculating #
  
  print("----------------------------------")
  print("---------- Savings: ")
  
  print("Business savings: R", round(savings_goals()[0],2))
  print("Emegency Funds: R", round(savings_goals()[1], 2))
  print("Fixed Savings: R", round(savings_goals()[2],2))
  print("----------------------------------")
  
  # Change After all spending
  
  print("Total Change: R", round((ent_expanses()[2]+monthly_expenses()[1]), 2))
  print("----------------------------------")
else:
  print("Invalid entry!")