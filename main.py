from cost import total_cost
from budget import cal_budget

destination = input("Which city will you be visting?\n")
days = int(input("How many days will you be visting for?\n"))
transport = input("What type of transportation will you be taking? (public/car)\n")

total = total_cost(destination, transport, days)

print("Flight Cost: $", total['flight'])
print("Hotel Cost: $", total['hotel'])
print("Transportion Cost: $", total['transport'])
print("Total Cost: $", total['total'])

budget = float(input("How much money do you currently have?\n"))
months = int(input("In how many months time do you plan to go to {}?".format(destination)))
cal_budget(budget, total['total'], months)
