# Programmer: [Darcy Ostrander]
# Course: CS701/GB-731, Dr. Yalew
# Date: [8/7/24]
# Programming Assignment: 3
# Program Inputs: A string containing answer
# Program Outputs: Very good(If 100% correct) or Missed number and Score Presentage

def main():
    # Define a string containing the correct answers.
    CORRECT_ANSWERS = "adbdcacbdac"
    # Have the user enter their exam answers and check if there is the correct amount.
    answers = input("Error: an incorrect number of answers given.")
    while len(answers) != 11:
        answers = input("Incorrect number of answers. Please enter answers again: ")
    # check exam by comparing answers and keeping track of the number of correct answers
    correct = 0
    answer_string = ""
    for i in range(0,11):
        if CORRECT_ANSWERS[i] == answers[i]:
            correct = correct + 1
            answer_string = answer_string + CORRECT_ANSWERS[i]
        else:
            answer_string = answer_string + "X"
    # grade the exam and display grade percent, comment if 100% scored
    grade = (correct/11) * 100
    
    if grade == 100:
        print("Very Good!")
    else:
        print("You missed " + str(11-correct) + " questions: " + answer_string)
    print("Your score is: %.0f percent" % grade)


if __name__ == "__main__":
    main()


