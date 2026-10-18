import random

""" item1 = "apples"
item2 = "bananas"
item3 = "oranges"
item4 = "grapes"

shopping_list = [item1, item2, item3, item4] """

shopping_list = ["oranges", "apples", "bananas", "oranges", "grapes", "oranges"]

#len()
""" print(f"We have {len(shopping_list)} items in our shopping list.") """

#append()
""" shopping_list.append(["pears", "kiwis", "mangoes"]) """

#extend()lisab loendisse mitu elementi korraga eraldi elementidena.
""" shopping_list.extend(["pears", "kiwis", "mangoes"]) """

#remove() eemaldab loendist esimese sobiva väärtuse.
""" shopping_list.remove("oranges") """

#teeme koopia ostunimekirjast, et vältida konflikte 
""" for item in shopping_list.copy():
    if item == "oranges":
        shopping_list.remove(item) """

#count()
""" n = shopping_list.count("oranges")

print(f"We have {n} oranges in our shopping list.") """

#index()
""" apple_index = shopping_list.index("apples")
shopping_list[apple_index] = "green apples" """

#found
""" found = False

for item in shopping_list:
    if item == "green apples":
        found = True
        break """

#süntaktiline viis, kuidas kontrollida, kas element on listis olemas, süntaktiline suhkur
""" found = "green apples" in shopping_list

if found:
    print("Green apples are in our shopping list.")
else:
    print("Green apples are not in our shopping list.") """


""" print(f"Apples are at index {apple_index} in our shopping list.") """

""" print(f"We have {len(shopping_list)} items in our shopping list.") """

print(shopping_list)

#sort muudab olemasolevat loendit ennast.
#sort() sorteerib ja reverse=True tähendab, et järjestus tehakse vastupidiseks ehk kahanevaks.
""" shopping_list.sort(reverse=True) """

#reverse
""" shopping_list.reverse() """

#random
random_item = random.choice(shopping_list)
print(random_item)

print(shopping_list)

# for item in shopping_list:
#     print(item)
    
""" sort() → Järjestab loendi elemendid kasvavas järjekorras.
indeks → Elemendi järjekorranumber loendis, algab nullist.
import → Käsk, millega tuuakse moodul programmi kasutamiseks.
remove() → Eemaldab esimese vastava elemendi loendist.
append() → Lisab ühe uue elemendi loendi lõppu.
reverse() → Pöörab olemasoleva loendi järjekorra vastupidiseks.
insert() → Lisab uue elemendi kindlale positsioonile loendis.
random → Moodul, mis võimaldab teha juhuslikke valikuid.
loend → Andmestruktuur, mis hoiab korraga mitut väärtust.
element → Üks väärtus, mis kuulub loendisse. """