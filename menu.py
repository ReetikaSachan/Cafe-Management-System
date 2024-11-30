#Menu of the restaurant
Menu = {
    'Tea' : 30,
    'Coffee' : 50,
    'Pasta' : 80,
    'Coldrink' : 40,
    'Onion pizza' : 100,
    'Capsicum pizza' : 100.
   
}

#Greet the client
print("Welcome to my restaurant")

#Show Menu
print("Tea : Rs.30\nCoffee : Rs.50\nPasta : Rs.80\nColdrink : Rs.40\nOnion pizza : Rs.100\nCapsicum pizza : Rs.100")

#Total sum of order
price = 0

item_1 = input("Enter your order : ") #first order
if item_1 in Menu:
    price += Menu[item_1] #0+80
    print("Your item",item_1,"has been added to your order")

else:
    print("Please order something")

#Second order
item = input("Do you want to add another item ? (Yes/No)")
if item == "Yes":
    item_2 = input("Enter your second order : ")
    if item_2 in Menu:
     price += Menu[item_2]
     print("Your item",item_2,"has been added to your order")
    else:
     print("Item is not available, Sorry")
     
else:
     print("Thank You")

print("The total of your bill is : ",price)





    
    

