#Control flow structures
#these specify flow of control in programs
#Types include;
# Conditional statements/flow: these statements base on particular conditions
#create a program that asks a user for the food type bought from the market
# the program should print you bought chicken if the user enters chicken
# the program should print you bought liver if the user enters liver
# else print fish 

food_type = input('Enter the food type bought: ').lower()

if food_type =="chicken":
  print(f"you bought chicken from the market")
elif food_type =="liver":
  print(f'you bought liver from the market')
else: 
  print(f'you bought fish from the market')

  #Approach one 
if food_type!= input("chicken") or food_type!=("liver") or food_type!=("fish"):
     print(f"you have entered a wrong food type:")
elif food_type == 'chicken':
    print(f"you bought chicken from the market")
elif food_type =="liver":
     print(f'you bought liver from the market')
else: 
     print(f'you bought fish from the market')

      


            
        