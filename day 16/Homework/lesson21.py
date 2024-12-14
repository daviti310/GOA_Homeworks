# ცვლადების შექმნა ლოგიკური ოპერაციების შედეგებით
a = True and False      # False: ლოგიკური "და" (AND) - ერთი მაინც თუ False-ია, შედეგიც False იქნება
b = True or False       # True: ლოგიკური "ან" (OR) - ერთი მაინც True თუა, შედეგიც True იქნება
c = not True            # False: ლოგიკური "არ" (NOT) - აბრუნებს საპირისპირო მნიშვნელობას
d = (5 > 3) and (2 < 4) # True: ორივე პირობა (5 > 3 და 2 < 4) მართალია
e = (10 == 5) or (7 != 8)  # True: ერთი პირობა (7 != 8) მართალია

print(a) # False
print(b) # True
print(c) # False
print(d) # True
print(e) # True

