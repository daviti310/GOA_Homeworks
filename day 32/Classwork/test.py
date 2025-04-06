string_list = ["apple", "banana", "cherry", "date", "elderberry"]

integer_list = [1, 2, 3, 4, 5]

float_list = [1.1, 2.2, 3.3, 4.4, 5.5]

boolean_list = [True, False, True, False, True]

big = [string_list] + integer_list + float_list + boolean_list
print(big)



product_list = ["Apple", "Banana", "Carrot"]

product_4 = "Milk"
product_5 = "Bread"
product_list.extend([product_4, product_5])

index = int(input("Enter the index of the product you want (0-4): "))
print(f"You selected: {product_list[index]}")
new_product = input("Enter a new product: ")
product_list[index] = new_product
print("Updated list:", product_list)
