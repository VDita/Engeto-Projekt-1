"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dita Velčevová
email: d.velcevova@gmail.com
discord: dita8703
"""


separator = ("-" * 40)
users = {
    "bob" : "123", 
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Vyžádám si od uživatele přihlašovací jméno a heslo
user = input("username: ")
password = input("password: ")
print(separator)

#Pokud se uživatelské jméno nebo heslo  neshoduje, pak upozorni a ukonči program
if not(users.get(user) == password):
    print("unregistered user, terminating the program..")

#Pokud sedí uživatelské jméno a heslo, pozdrav a umožni analyzovat text 1, 2 nebo 3
else:
    print("Welcome to the app,", user)
    print("We have 3 texts to be analyzed")
    print(separator)
    select_text = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)

#Pokud uživatel vybere jiné číslo než 1, 2 nebo 3, nebo zadá jiný znak, tak se program ukončí
if not(select_text.isdigit() and 1 <= int(select_text) <= 3):
        print("Selected text is not in range, terminating the program..")

#Pokud vybere správně, tak začne analýza textu
else:
        #Počet slov
        selected_text = TEXTS[int(select_text) - 1]
        words = len(selected_text.split())
        print("There are", words, "words in the selected text.")
        
        #Počet slov začínajících velkým písmenem
        titlecase = sum(word[0].isupper() for word in selected_text.split())
        print("There are", titlecase, "titlecase words.")
        
        #Počet slov psaných velkými písmeny
        uppercase = sum(word.isupper() and word.isalpha() for word in selected_text.split())
        print("There are", uppercase, "uppercase words.")
        
        #Počet slov psaných malými písmeny
        lowercase = sum(word.islower() for word in selected_text.split())
        print("There are", lowercase, "lowercase words.")
        
        #Počet čísel (ne cifer)
        numeric = sum(word.isnumeric() for word in selected_text.split())
        print("There are", numeric, "numeric strings.")
        
        #Suma všech čísel (ne cifer) v text
        sum_numeric = 0
        text = selected_text.split()
        for word in text:
            if word.isdigit():
                sum_numeric += int(word)
        print("The sum of all the numbers", sum_numeric)
        print(separator)
        
        #Jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu
        word_len = {}
        for word in text:
            lenght = len(word.strip(".,!?;:"))
            if lenght > 0:
                if lenght in word_len:
                    word_len[lenght] += 1
                else:
                    word_len[lenght] = 1
        print("{:<4}| {:<20} | NR.".format("LEN", "OCCURRENCES"))
        print(separator)
        for lenght, word_sum in sorted(word_len.items()):
            print("{:<4}| {:<20} | {}".format(lenght, '*' * word_sum, word_sum))