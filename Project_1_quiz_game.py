from tkinter.messagebox import YES


print("Hey! Welcome to the quiz.")
playing = input("Do you want to play? \n")
if playing.lower() != "yes":
    quit()
print("Okay! Let's start playing quiz game!")
score = 0

question1 = input("What is the full form of CPU? \n")
if question1.lower() == "central processing unit":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1
    
question2 = input("Who is the father of computer? \n")
if question2.lower() == "charles babbage":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question3 = input("Which of the following language does the computer understand? Binary Language or C Language? \n")
if question3.lower() == "binary language":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question4 = input("What is called the brain of the computer? CPU or Control Unit? \n")
if question4.lower() == "cpu":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question5 = input("What is the smallest unit of data in computer system? Bit or nibble? \n")
if question5.lower() == "bit":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question6 = input("Which device provides the communication between a computer and the outer world? I/O or Compact? \n")
if question6.lower() == "i/o":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question7 = input("Which of the following can access the server? Web Client, Web Server or Web Browser? \n")
if question7.lower() == "web client":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question8 = input("Which of the following is not a type of computer on the basis of operation? Hybrid, Remote or Analog? \n")
if question8.lower() == "remote":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

question9 = input("Which of the following is the first neural network computer? SNARC, RFD or AM? \n")
if question9.lower() == "snarc":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1
    
question10 = input("A computer cannot 'boot' if it does not have the...? Compiler or Operating System? \n")
if question10.lower() == "operating system":
    print("Correct Answer!")
    score += 4
else:
    print("The Answer is incorrect!")
    score -= 1

    print("You got " + str(score) + " marks!")
    print("You got " + str((score/40)*100) + "%"" score!")