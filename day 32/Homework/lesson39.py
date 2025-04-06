'''მომხმარებელს შეაყვანინე ინდექსი და ახალი ფერი, შეცვალე ამ ინდექსზე არსებული ფერი სიაში `colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]` და დაბეჭდე განახლებული სია'''

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("Enter an index: "))
new_color = input("Enter the new color: ")

if 0 <= index < len(colors):
    colors[index] = new_color
    print(colors)
else:
    print("Invalid index!")