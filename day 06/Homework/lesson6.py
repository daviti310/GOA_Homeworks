# წიგნების თავდაპირველი ფასები
book_price_1 = 25.99  # წიგნის 1 თავდაპირველი ფასი
book_price_2 = 15.50  # წიგნის 2 თავდაპირველი ფასი
book_price_3 = 30.00  # წიგნის 3 თავდაპირველი ფასი
book_price_4 = 22.75  # წიგნის 4 თავდაპირველი ფასი
book_price_5 = 18.90  # წიგნის 5 თავდაპირველი ფასი

# ფასდაკლების ოდენობა (მაგალითად 10% ფასდაკლება)
discount_percentage = 0.10

# ახალი ფასები, ფასდაკლების შემდეგ
new_book_price_1 = book_price_1 * (1 - discount_percentage)  # წიგნის 1 ახალი ფასი
new_book_price_2 = book_price_2 * (1 - discount_percentage)  # წიგნის 2 ახალი ფასი
new_book_price_3 = book_price_3 * (1 - discount_percentage)  # წიგნის 3 ახალი ფასი
new_book_price_4 = book_price_4 * (1 - discount_percentage)  # წიგნის 4 ახალი ფასი
new_book_price_5 = book_price_5 * (1 - discount_percentage)  # წიგნის 5 ახალი ფასი

print(new_book_price_1) # დაბეჭდილი წიგნის 1 ახალი ფასი
print(new_book_price_2) # დაბეჭდილი წიგნის 2 ახალი ფასი
print(new_book_price_3) # დაბეჭდილი წიგნის 3 ახალი ფასი
print(new_book_price_4) # დაბეჭდილი წიგნის 4 ახალი ფასი
print(new_book_price_5) # დაბეჭდილი წიგნის 5 ახალი ფასი