print("Welcome to weight converter app")
weight = int(input("Weight: "))
weight_type = input("Is it in Kg (K) or Lbs (L)?: ")
if weight_type.lower() == 'l':
    final_weight = weight*0.45
    print(f"Your weight is {final_weight} Kgs")
elif weight_type.lower() == 'k':
    final_weight = weight / 0.45
    print(f"Your weight is {final_weight} Lbs")


