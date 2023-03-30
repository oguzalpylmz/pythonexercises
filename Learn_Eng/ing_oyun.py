import random
print("Welcome to Word Riddle Game")
print("""---------------------------
""")

def openFile():
    global words
    global english_words

    words = {}

    english_words = []

    with open("C:/Users/oguza/OneDrive/Masaüstü/word_list.txt","r",encoding = "utf-8") as file:
              for a in file:
                a = a[:-1]
                english , turkish = a.split(",")
                words[english] = turkish
    
    for a in words:
        english_words.append(a)

    random.shuffle(english_words)

def game():
    a = 0
    b = 1
    c = 2
    d = 3
    letters = [a,b,c,d]


    while True:
            random.shuffle(letters)
            print("1-) {}  2-) {}  3-) {}  4-) {}".format(english_words[a].capitalize(),english_words[b].capitalize(),english_words[c].capitalize(),english_words[d].capitalize()))
            print("""Which word is equal the {} in Turkish?""".format(words[english_words[letters[0]]].capitalize()))



            answer = input("Answer => ")   
            if english_words[int(answer)-1] == english_words[letters[0]]:
                print("""Well Done!! You are right!
                """)
            else:
                print("Wrong Answer :(")
                print("""
{} = {} | {} = {} | {} = {} | {} = {}
----------------------------------------
                    """.format(english_words[a].capitalize(),words[english_words[a]].capitalize(),english_words[b].capitalize(),words[english_words[b]].capitalize(),english_words[c].capitalize(),words[english_words[c]].capitalize(),english_words[d].capitalize(),words[english_words[d]].capitalize()))


            del english_words[0]
            
            del english_words[0]
            
            del english_words[0]
            
            del english_words[0]


            if c >= len(english_words) - 1:
                print("You answered all questions!")
                break
                 
openFile()
game()