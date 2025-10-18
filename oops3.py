import random
class fruitquiz:
    def __init__(self):
        self.fruits={"apple":"red","orange":"orange","watermelon":"green","banana":"yellow","grape":"purple"}
    
    def quiz(self):
        while True:

            fruit,colors=random.choice(list(self.fruits.items()))

            print("What is the color of{}?".format(fruit))
            user_answer=input()

            if user_answer.lower()==colors:
                print("Correct!")
            else:
                print("Wrong")
            
            option=input("Enter 0 to stop the quiz else enter 1 to continue:")

            if(option):
                break

print("Welcome to Fruit Color Quiz")
fq=fruitquiz()
fq.quiz()