temp = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if 10 <= temp <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon" or time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

if 18< temp <= 24:
    if time_of_day == "Morning" or time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"

if temp >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")