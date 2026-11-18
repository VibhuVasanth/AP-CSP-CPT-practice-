#Hello, This is my Nutruion Analyer by Vibhu Vasanth 


# Defined everything down below
food_eaten = []
calories_food = []
quantities = []
food_groups = []


total_calories = 0


print("Welcome to Nutrition Analyzer")


while True:
  food = str(input("Please enter a food one by one(eg. chicken) "))

  if food.lower() == "done":
    break

  while True:
    calories = int(input("Enter calories how much calories this had(eg.150 calories of one chicken) "))

    if calories != int:
      print("Please enter a valid input")
  if calories == "done":
      print("okay name the quanitites of each of your foods ")
while True:
    quantity = input("Enter the quantity:")
    if quantity != int:
      print("Please enter a valid quantity")
    
    

      

    food_eaten.append(food)
    calories_food.append(calories)
    quantities.append(quantity)
  
    #This is the myplate portion 
  
  
    protein = int(input("How many protien calories did you have? "))
    carbs   = int(input("How many calories of cabrs did you eat? "))
    vegetables = int(input("How any calories from vegetables? "))
    fruits = int(input("How many calories did you get from Fruits? "))
    fats = int(input("How many calories from fats? "))
    dairy = int(input("How many calories from dairy? "))
  

  #Functions 

def analyze_nutruiton(food_eaten, calories, quantities, protien, carbs, vegetables, fruits, fats, dairy):


    total =  0

    for i in range(len(food_eaten)):
      total = total + (calories[i]* quantities[i])
  
  
  

print("\n ------------------------Nutrition Report---------------------------")
while True:
 
  for i in range(len(food_eaten)):
       print("Food:", food_eaten)
       print("Calories,", calories_food[i])
       print("Quantity,", quantities[i])
       print("Total" ,calories_food[i] * quantities)
  if protein == 0:
        print("Try including a more protien in your diet")
  if protein > 350:
        print("You have way to much protein in your diet, decrease your protien intake")
  if vegetables == 0:
        print("Try including more vegetables ")
  if vegetables >350:
        print("Try to decrease the amount of veggie calories your having ")
  
  if fruits == 0:
        print("Try including more fruits in your diet")
  if fruits >350:
        print("Try to decrease the amount of fruits  calories your having ")
  if fats == 0:
        print("Add more fats in your diet")
  if fats >350:
        print("Try to decrease the amount of fat calories your having ")
  if dairy == 0:
        print("Add more dairy into your diet")
  if dairy >350:
        print("Try to decrease the amount of dairycalories your having ")
  
  done= input("Would you Like to do it again (Y/N")
  if done == "Y":
        continue
  if done == "N":
        print("Thank you for using the Nutriton Analyzer")
        break
                 
  
  
      
  
