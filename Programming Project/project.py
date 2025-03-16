def login():
    
    # Initialize an empty dictionary
    login_credentials = {}
    
    # Get user input for key and value
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    # Append the user input (key:value pair) to dictionary
    login_credentials[username] = password
    
    login_info(login_credentials)


def login_info(login_credentials):                                                                                    
    CORRECT_LOGIN_CREDENTIALS = {"PGR107" : "Python" }
    if login_credentials == CORRECT_LOGIN_CREDENTIALS:
        print("***Login successful***\n")
        play_quiz(1)
    else:
        print("***Invalid username and/or password***\n")
        login()
 
        
def print_quiz(quiz_number):
    my_quizes = {
        1: "Q1. What is the capital of Norway?\n" 
                      + "a. Bergen\n" 
                      + "b. Oslo\n"
                      + "c. Stavanger\n"
                      + "d. Trondheim\n" ,
        2: "Q2. What is the currency of Norway?\n"
                      + "a. Euro\n"
                      + "b. Pound\n"
                      + "c. Krone\n"
                      + "d. Deutshe Mark\n",
        3: "Q3. What is the largest city in Norway?\n"
                         + "a. Oslo\n"
                         + "b. Stavanger\n"
                         + "c. Bergen\n"
                         + "d. Trondheim\n",
        4: "Q4. When is constitution day (the national day) of Norway?\n"
                         + "a. 27th May\n"
                         + "b. 17th May\n"
                         + "c. 17th April\n"
                         + "d. 27th April\n",
        5: "Q5. What color is the background of the Norwegian flag?\n"
                         + "a. Red\n"
                         + "b. White\n"
                         + "c. Blue\n"
                         + "d. Yellow\n",
        6: "Q6. How many countries does Norway border?\n"
                         + "a. 1\n"
                         + "b. 2\n"
                         + "c. 3\n"
                         + "d. 4\n",
        7: "Q7. What is the name of the university in Trondheim?\n"
                        + "a. UiS\n"
                        + "b. Uio\n"
                        + "c. NMBU\n"
                        + "d. NTNU\n",
        8: "Q8. How long is the border between Norway and Russia?\n"
                        + "a. 96 km\n"
                        + "b. 196 km\n"
                        + "c. 296 km\n"
                        + "d. 396 km\n",
        9: "Q9. Where in Norway is Stavanger?\n"
                        + "a. North\n"
                        + "b. South\n"
                        + "c. South-west\n"
                        + "d. South-east\n",
        10: "Q10. From which Norweigian city did the world's famous composer Edvard Grieg come?\n"
                        + "a. Oslo\n"
                        + "b. Bergen\n"
                        + "c. Stavanger\n"
                        + "d. Tromsø\n"                        
        }
    print(my_quizes[quiz_number])

def return_correct_answer(quiz_number):
    correct_answers = {
        1: "b",
        2: "c",
        3: "a",
        4: "b",
        5: "a",
        6: "c",
        7: "d",
        8: "b",
        9: "c",
        10: "b"
        }
    
    return correct_answers[quiz_number]

def play_quiz(quiz_number):
    number_of_correct = 0
    number_of_wrong = 0
    
    # lists to hold the the question itself, the correct answer and the users wrong answer
    question_answerd_wrong = []
    correction = []
    user_wrong_answer = []
    
    while quiz_number <= 10:
        print_quiz(quiz_number)
        user_answer = input("Enter your answer: ")
        print("--------------------------------------\n")   

        correct_answer = return_correct_answer(quiz_number)
        
        if user_answer == correct_answer:
            number_of_correct += 1
        else:
            number_of_wrong += 1
            correction.append(correct_answer)
            question_answerd_wrong.append(quiz_number)
            user_wrong_answer.append(user_answer)
            
        quiz_number = quiz_number + 1
      

# At the end of the quiz
    if quiz_number > 10:
        display_number_of_correct_and_incorrect_answers(
            number_of_correct,
            number_of_wrong
        )
        
        display_question_and_incorrect_and_correct_answers(
            number_of_wrong,
            question_answerd_wrong,
            user_wrong_answer, 
            correction
        )
                

def display_number_of_correct_and_incorrect_answers(
        number_of_correct,
        number_of_wrong
):
    print("\n***********Quiz ended!**********")
    print("***********YOUR RESULT**********\n")
    print(f"Number of correct: {str(number_of_correct)}")
    print(f"Number of incorrect: {str(number_of_wrong)}\n")
    
    
    

def display_question_and_incorrect_and_correct_answers(
        number_of_wrong,
        question_answerd_wrong,
        user_wrong_answer,
        correction
):
    i = 0
    
    while i < number_of_wrong:
        print("*****For your incorrect answer*****")
        # print(f"You got question {question_answerd_wrong[i]}.\n" )
        print_quiz(question_answerd_wrong[i])
        print(f"Your answer was {user_wrong_answer[i]}, the correct answer is {correction[i]}.\n")
        i += 1
    
    
    
def main():
    login()
    
# start the program.
main()