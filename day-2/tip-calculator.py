print("Welcome to the tip calculator")
bill = int(input("Enter the total bill:"))
tip = int(input("Enter the tip percenetage you would like to tip: 10, 12 or 20:"))
persons = int(input("How many people should split it:"))

tipAmt = bill * tip / 100
totalBill = bill + tipAmt
perPerson = totalBill / persons

print(f"Each person should pay: {round(perPerson, 2)}")

