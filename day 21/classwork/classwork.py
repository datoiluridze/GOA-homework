# 1) კომენტარების საშუალებით ახსენით განსხვავება insert და append შორის
# 1) insert da append-ს შორის განსხვავებაა რომ appends-ს შეუძლია ბოლოში ჩააგდოს item და მისამართის მიცემას ვერ შეძლებ
#  instert-ით შეგიძლია მისამართი/index დაუწერო და ნებისმიერ itemების შორის ჩაწეროს სიტყვა

# 2) მომხმარებელს შემოატანინეთ  თავიანთი გვარი და len ფუნქციის გამოყენებით გამოიტანეთ გვარის სიგრძე
gvari = input("please enter your last name: ") 
raodenoba = len(gvari) 
print("Number of characters:", raodenoba) 

# 3) movies = ["Avatar", "Titanic", "Avengers", "GOA" , "Group 30"] ამ სიაში 3 ინდექსად ჩასვით თქვენი სახელი
movies = ["Avatar", "Titanic", "Avengers", "GOA" , "Group 30"]
movies.insert(3, "Dato")
print(movies)

# 4) cars = ["BMW",  "Audi", "Honda"] list ბოლოში დაამატეთ თქვენი საყვარელი მანქანა 
cars = ["BMW",  "Audi", "Honda"]
cars.append("GTR")
print(cars)