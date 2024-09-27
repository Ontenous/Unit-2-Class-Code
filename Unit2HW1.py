"""
Name: William Nathan
Date: 9/27/24
Description: Unit 2 homework 2
"""

print('Problem 1'.center(20,'-'))

print("One of my Dungeons and dragons games")
print("Going through a dungeon")
print("Pet shopping trip")

print('Problem 2'.center(20,'-'))

print(f"""       __             _,-"~^"-.
     _// )      _,-"~`         `.
   ." ( /`"-,-"`                 ;
  / 6                             ;
 /           ,             ,-"     ;
(,__.--.      \           /        ;
 //'   /`-.\   |          |        `._________
   _.-'_/`  )  )--...,,,___\     \-----------,)
 ((("~` _.-'.-'           __`-.   )         //
   jgs ((("`             (((---~"`         //
                                          ((________________
                                          `----""""~~~~^^^```""")

print('Problem 3'.center(20,'-'))

mile_total = 173.8
fuel_efficiency = float(input("How many miles does your car get per gallon? "))
gas_price = float(input("How much does a gallon of gas cost near you? "))
tank = int(input("How many gallons does your car's tank hold? "))
price = ((gas_price*tank) % fuel_efficiency)*mile_total
rounded_price = round(price,2)

print(f"To drive to Seattle from Portland, it would cost you ${rounded_price}")