'''მომხმარებელს შემოატანინეთ რიცხვი, შეინახეთ ის ცვლადში და გაამრავლეთ ორზე, შემდეგ კი დაუბეჭდეთ წინადადება ფორმატით: 'Your number multiplied by 2 is <number>' სადაც <number>-ის ნაცვლად ჩაწერეთ 2-ზე გამრავლებულ რიცხვს, გამოიყენეთ ხელოვნური მონაცემტა ტიპის შეცვლა, input-იდან მიღებული მნიშვნელობა გარდაქმენით ჯერ integer ტიპად შემდეგ კი string-ად. ახსენით კომენტარებით თუ როგორ შეასრულეთ დავალება'''

# ახლა ვქმნი პირველ ცვლადს სადაც მომხმარებელს შევატანინებ თავის საყვარელ რიცხვს
num1 = int(input("enter your favorite number: "))

# ახლა ვქმნი მეორე ცვლადს სადაც პირველი ცვლადი მრავლდება მეორეზე
num2 = num1 * 2

# ახლა ვბეჭდავ წინაადებას Your number multiplied by 2 is <num2>
print("Your number multiplied by 2 is" + " " + str(num2))

