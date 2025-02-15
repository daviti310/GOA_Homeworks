"""მომხმარებელს შეეკითხეთ სახელი და იქამდე არ შეეშვათ (განმეორებითად ჰკითხეთ) სანამ თქვენს სახელს არ შემოიყვანს"""

name = input("Enter your name: ")
while name != "Daviti":
    print("Try again!")
    name =input("Enter your name: ")