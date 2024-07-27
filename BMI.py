# weight = float(input("Your weight : "))
# height = float(input("Your height : "))
# result = weight//height**2
# # print("Your BMI = ", int(result))
# print(f"For weight = {weight} and height = {height} so your BMI = {result}")
# # print("For weight = {} and height = {} so your BMI = {}" .format(*args: weight,height,result))

print("=====Welcome to the tip calculator=====")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 20, 30 ?"))
people = int(input("How many people to split the bill? " ))
tip_amount = bill*tip/100
total = bill+tip_amount
each_pay = total/people
print(f"Each person should pay {each_pay}$")



