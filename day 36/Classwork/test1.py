'''შექმენით სია რომელშიც ჩამოწერთ მინიმუმ 10 პროგრამირების ენას, შემდეგ ამ სიაში მყოფი თქვენთვის ყველაზე არასასურველი ენა ჩაანაცვლეთ ახლით. საბოლოოდ კი slicing-ის გამოყენებით გამოიტანეთ სიის ნაწილები:

დადებითი slicing:
პირველიდან 5-ის ჩათვლით
2-დან ბოლომდე
4-დან 8-მდე

უარყოფითი:

მეექსვედან ბოლომდე
მეექვსემდე ყველაფერი
მეექვსეს ჩათვლით თავიდან ყველაფერი

ბონუს:
მთელი სია გამოიტანეთ თავიდან ბოლომდე შემობრუნებულად'''


programing_language = ['Python', 'Javascript', 'SQL', 'Java', 'PHP', 'C#', 'C++', 'Ruby', 'Swift', 'Rust']
programing_language[9] = 'Typescript'
print(programing_language[:6])
print(programing_language[1:10])
print(programing_language[3:7])
print(programing_language[-6:])
print(programing_language[:-5])
print(programing_language[:6])
print(programing_language[::-1])