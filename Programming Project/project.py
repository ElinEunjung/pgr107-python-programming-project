def login():
    
    # Initialize an empty dictionary
    login_credentials = {}
    
    # Get user input for key and value
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    
    # Append the user input (key:value pair) to dictionary
    login_credentials[username] = password
    
    # print(login_credential)
    login_info(login_credentials)


def login_info(login_credentials): 
    if login_credentials['PGR107'] == 'Python':
        print("***login successful***")
        print()
        play_quiz(1)
    else:
        print("***Invalid username and/or password***")
        print()
        login()
 
        
def print_quiz(quiz_number):
    my_quizes = {
        1: "Q1. What is the capital of Norway?\n" 
                           + "a. Bergen\n" 
                           + "b. Oslo\n"
                           + "c. Stavanger\n"
                           + "c. Trondheim\n" ,
        2: "Q2. What is the currency of Norway?\n"
                      + "a. Euro\n"
                      + "b. Pound\n"
                      + "c. Krone\n"
                      + "d. Deutshe Mark\n"
        }
    
    return print(my_quizes[quiz_number])

def print_correct_answer(quiz_number):
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
    
    return print(correct_answers[quiz_number])

def play_quiz(quiz_number):
    print_quiz(quiz_number)
    user_answer = input("Enter your answer: ")
    correct_answer = print_correct_answer(quiz_number)
    
    if user_answer == correct_answer:
        print("Correct!🥳")
        print_quiz(quiz_number + 1)
    else: 
        print_quiz(quiz_number)
        print("Your Answer:" + user_answer)
        print("Correct_Answer:" + correct_answer)
        print_quiz(quiz_number)

def main():
    login()
    
# start the program.
main()