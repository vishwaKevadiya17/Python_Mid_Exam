
print("======================================================================================")
print("======================================================================================")

print("Welcome to the Bill Splitter App!")

print("======================================================================================")
print("======================================================================================")


#User Inputs 

total_bill_amount = float(input("Enter Total Bill amount: "))

no_people = int(input("Enter number of people: "))

tip_per = int(input("Enter tip percentage (0/5/10/15/20):"))



#Validation using control structure


if no_people <= 0:
    print("This is Not valid, Enter Again No. of people.")

if total_bill_amount or tip_per < 0:
    print("Negative value not valid.")


#Calculations


tip_amount = (tip_per / 100 ) * total_bill_amount

final_bill = total_bill_amount + tip_amount

per_person = final_bill / no_people

#Display all value properly

print(f"Tip Amount: Rs.{tip_amount}")
print(f"Total Bill (with Tip): {final_bill} ")
print(f"Each person should pay: Rs.{per_person}")


#Using while loop to continue or exit based on user input (y/n)

yes_no = input("Would you like to calculate another bill? (y/n): ")

while yes_no == "y":
    print("======================================================================================")
    print("======================================================================================")
   
    print("Welcome to the Bill Splitter App!")
   
    print("======================================================================================")
    print("======================================================================================")
   
   
   #User Inputs 
   
    total_bill_amount = float(input("Enter Total Bill amount: "))
   
    no_people = int(input("Enter number of people: "))
   
    tip_per = int(input("Enter tip percentage (0/5/10/15/20):"))
   
   
   
   #Validation using control structure
   
   
    if no_people <= 0:
       print("This is Not valid, Enter Again No. of people.")
   
    if total_bill_amount or tip_per < 0:
       print("Negative value not valid.")
   
   
   #Calculations
   
   
    tip_amount = (tip_per / 100 ) * total_bill_amount
   
    final_bill = total_bill_amount + tip_amount
   
    per_person = final_bill / no_people
   
   #Display all value properly
   
    print(f"\nTip Amount: Rs.{tip_amount}")
    print(f"\nTotal Bill (with Tip): {final_bill} ")
    print(f"\nEach person should pay: Rs.{per_person}")
   
   
   #Using while loop to continue or exit based on user input (y/n)
   
    yes_no = input("Would you like to calculate another bill? (y/n): ")




                    
            
      







