'''მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
A თუ score მეტია 80-ზე
B თუ score მეტია 60-ზე
C თუ score მეტია 40-ზე
D თუ score მეტია 20-ზე
F თუ score 20-ზე ნაკლებია'''


score = int(input("Enter your score: "))
if score > 80:
    grade = "A"
else:
    if score > 60:
        grade = "B"
    else:
        if score > 40:
            grade = "C"
        else:
            if score > 20:
                grade = "D"
            else:
                grade = "F"
print(grade)