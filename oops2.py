class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
    
flash=[]
print("Welcome to Flashcards App")

while True:
    word=input("Enter a word you want to add to flashcard:")
    meaning=input("Enter its meaning:")

    flash.append(flashcards(word,meaning))
    option=input("Enter 0 if you want to stop adding flashcards else enter 1:")

    if(option):
        break
print("\nYour Flashcards")
for i in flash:
    print(">",i)

