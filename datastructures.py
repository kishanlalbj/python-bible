# List

list = ["Egg", "Milk", 12, True, 23.03]
print(list[4])

nested_list = [1,2,3,["Ram","Lakshman","Raavan"],4,5]
print(nested_list[2])
print(nested_list[3][0])

higher_order_nested_list = [[1,2,3, [4,5,6]]]
print(higher_order_nested_list[0][3][2])

# Travis Security

known_users = ["Kishan", "Raghav", "John Marchi", "Frank", "Ashwin", "Sravan"]

print("Hi.. I am Travis..The Gate Keeper")
name = input("What is your name?: ")
if name in known_users:
    print("Access Granted")
    remove = input("Do you want to be removed from System? (y/n)").lower()
else:
    print("Access Denied")



