# while True:
#     num = float(input())
#     if 1 < num < 100:
#         print(f"The number {num} is between 1 and 100")
#         break


number = float(input())

while number < 1 or number > 100:
    number = float(input())

print(f"The number {number} is between 1 and 100")