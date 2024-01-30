rate = (input("What is the current exchange rate from Euros to Dollars?"))
rate = float(rate)
amount = (input("What is the amount of currency you would like to exchange?"))
amount = float(amount)
total = float(amount * rate)
servicefee = 3
result = float(total - servicefee)
print (result)
