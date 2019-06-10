def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter Option: ")
    return option
    
def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file: # No need to add a file.close() at end of a 'with' block
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines): # The Enumerate function will turn the lists into a tuple. Line number = i and text in 'text'.
        if i%2 == 0: # If the line number 'i' is even, then = Question.
            questions.append(text)
        else: # If line number is odd, then = Answer.
            answers.append(text)
            
    number_of_questions = len(questions) # Function to check the length of the questions list.
    questions_and_answers = zip(questions, answers) # Call the Zip function. Prevents us from having to run the Zip function every time the 'for' loop is run. 
    
    score = 0
            
    for question, answer in zip(questions, answers): # Zip functions put both the question & answer lists together
        guess = input(question + "> ")
        if guess == answer: # if the user guess = answer, then correct & score increments by +1.
            score += 1
            print("That's Right!")
            print(score)
        else:
            print("That's Wrong!")
            
    print("You got {0} correct out of {1}".format(score, number_of_questions)) # Message appears at the end of the quiz.

def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open("questions.txt","a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid Option") # else is based upon a False boolean.
        print("") # creates a blank line for cosmetic reason.
        
game_loop() # this game loop will continue to run forever.



        