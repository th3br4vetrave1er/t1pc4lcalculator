print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num_of_customers = int(input("How many people to split the bill? "))
tip_percantage = tip / 100
total_tip = bill * tip_percantage
total_bill = round(total_tip + bill, 2)
bill_splited = round(total_bill / num_of_customers, 2)
print(f"Total bill is ${total_bill}. Each person should pay ${bill_splited}")