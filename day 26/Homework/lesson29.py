#მომხმარებელს შემოატანინეთ 2 რიცხვი, შემდეგ კი ამ ორ რიცხვს შორის არსებული ყველა რიცხვის ჯამი გაიგეთ for ციკლის გამოყენებით უმციერსიდან უდიდესამდე. საბოლოოდ დაბეჭდეთ ეს ჯამი


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


start = min(num1, num2)
end = max(num1, num2)

sum_numbers = 0


for i in range(start, end + 1):
    sum_numbers += i

print("The sum of the numbers is:", sum_numbers)
