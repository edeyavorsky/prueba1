Option = int(input("Please Enter A Valid Option: \n1- Vegetarian \n2- Non Vegetarian\n->"))
if Option == 1:
    Ingredient = int(input("Please Enter A Valid Option: \n1- Pimiento \n2- Tofu\n->"))
    if Ingredient == "1":
        Ingredient = "Pimiento"
    else:
        Ingredient = "Tofu"
    print("The pizza is Vegetarian and has these ingredients: Tomato, Mozarella and {Ingredient}")
elif Option == 2:
    Ingredient = int(input("Please Enter A Valid Option: \n1- Peperoni\n2- Jamon\n3- Salmon \n->"))
    if Ingredient == 1:
        Ingredient = "Peperoni"
    elif Ingredient == 2:
        Ingredient = "Jamon"
    else:
        Ingredient = "Salmon"
else:
    print ("Invalid Option")