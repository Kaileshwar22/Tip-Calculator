print("welcome to tip calculator")
bill = float (input("what is yor total bill "))

percentage = int(input("what percentage you wanna spilt?10,12,15 "))

people = int (input("how many people "))
tip_as_percent = percentage/100
total_tip = bill*tip_as_percent
total_bill = bill+total_tip
bill_per_person = total_bill/people
final_bill = round(bill_per_person,2)
print(final_bill)




