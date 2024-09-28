# 1) დღეს ნასწავლი მეთოდები ყველა ჩამოწერეთ მიუწერეთ მათი ფუნქციები და დაუწერეთ 2-2 მაგალითი

# 2) მომხმარებელს შემოატანინეთ მისი სახელი და სახელიდან 2 ინდექსზე მდგომი ასო ამოშალეთ(ისევე როგორც ლისტებზე ვაკეთებდით)

name = input("please enter your name: ")

print(name[:2]+name[3:])

# 3)შექმენით სია ქვეყნების. გამოიყენეთ pop() და წაშალეთ მეორე ქვეყანა შემდეგ გამოიტანეთ ორივე წაშლილი ქვეყანაც და ახალი სიაც

countrys = ["Georgia", "Latvia", "France", "Japan"]
print(countrys.pop(1))
print(countrys)

# 4) numbers = [10, 20, 30] ლისტში insert მეთოდით 10 და 20 შუაში ჩაამატეთ 15

numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

# 5) შექმენით ცარიელი სია. სიას სათითაოდ დაუმატეთ "Dog" "cat" და "bird" და დაბეჭდეთ საბოლოო სია.

animal = []
animal.append("dog")
animal.append("cat")
animal.append("bird")
print(animal)