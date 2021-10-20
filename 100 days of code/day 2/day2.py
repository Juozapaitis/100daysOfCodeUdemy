print("Welcome to the tip calculator.")

totalBill = float(input("What is the total bill? $ "))
people = int(input("How many people to split the bill? "))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

forEach = (totalBill + (totalBill * (tipPercent / 100))) / people
final_amount = "{:.2f}".format(forEach)
print(f"Each person should pay: ${final_amount}")

