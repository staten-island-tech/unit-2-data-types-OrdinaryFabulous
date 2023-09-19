# << Contains All Challenge Codes + MadLib >> # 
#   1. Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments. Then craft the function. 
#   2. Mad Libs Project
#   3. Let's create a function that determines if a number is odd or even
#   4. Let's create a function to accept a "bill" value and offer a tip of 0%, 15%, 20% or 25% depending on if the service was "bad, okay, good , or great ". 
#   5. Create a function that accepts an input and determines all factors of the number. 
#   6. Create a function that accepts 2 arguments. Find the greatest common factor between those numbers. 

# << Challenge 1 >> #
def CountWord():
    String = input("Please Input A String: ")
    print(f"Your String Has {len(String.split())} Words")

# << Challenge 2 >> #
def MadLibs():
    Name1 = input("Please input a name: ")
    Noun1 = input("Please input a noun: ")
    Verb1 = input("Please input a verb: ")
    Verb2 = input("Please input another verb: ")
    Celebrity1 = input("Please input a celebrity's name: ")

    print(f"""Today was a boring day. 
{Name1} {Verb1} to school and sat down in homeroom. 
Suddenly {Celebrity1} showed up into class, it was a surprise for all the students and they were excited.
{Name1} did not expect much to happen but then they triped on a {Noun1} and fell down the stairs and broke their neck.
{Name1} woke up in a hostipial shortly after but {Verb2} back to school""")
    
# << Challenge 2 >> #
def odd(num: int):
    if num%2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

# << Challenge 3 >> #
def bill(billvalue: int):
    SRating = ["bad", "okay", "good", "great"]
    GRating = False

    ServiceRating = input(f"Your Current Bill is: ${billvalue}. How was the service? Input Bad, Okay, Good, or Great: ")
    if ServiceRating in SRating:
        GRating = True

    while not GRating:
        ServiceRating = input(f"Please input a valid rating of 'Bad', 'Okay', 'Good', or 'Great' only. ")
        if ServiceRating.lower() in SRating:
            GRating = True
    
    Confirmation = False

    while not Confirmation:
        if ServiceRating.lower() == "bad":
            print(f"Your total bill will be ${billvalue}")
            Confirmation = True

        elif ServiceRating.lower() == "okay":
            Confirm = input(f"Your current bill is {billvalue}, would you like to add a tip of 15%? (Total will be ${billvalue * 1.15})")

            if Confirm.lower() != "yes" and Confirm.lower() != "no":
                Confirm = input(f"Please Input A Valid Answer (Yes and No Only)")
            elif Confirm.lower() == "yes":
                print(f"Your total will be {billvalue * 1.15}")
            elif Confirm.lower() == "no":
                print(f"Your total will be ${billvalue}")

        elif ServiceRating.lower() == "good":
            Confirm = input(f"Your current bill is {billvalue}, would you like to add a tip of 15%? (Total will be ${billvalue * 1.20})")

            if Confirm.lower() != "yes" and Confirm.lower() != "no":
                Confirm = input(f"Please Input A Valid Answer (Yes and No Only)")
            elif Confirm.lower() == "yes":
                print(f"Your total will be {billvalue * 1.20}")
            elif Confirm.lower() == "no":
                print(f"Your total will be ${billvalue}")

        elif ServiceRating.lower() == "great":
            Confirm = input(f"Your current bill is {billvalue}, would you like to add a tip of 15%? (Total will be ${billvalue * 1.25})")

            if Confirm.lower() != "yes" and Confirm.lower() != "no":
                Confirm = input(f"Please Input A Valid Answer (Yes and No Only)")
            elif Confirm.lower() == "yes":
                print(f"Your total will be {billvalue * 1.25}")
            elif Confirm.lower() == "no":
                print(f"Your total will be ${billvalue}")
                
# << Challenge 4 >> #
def factorout(num):
    factorlist = []

    # << Run through each number from 0 to the number (a number cannot have a factor bigger than the number itself) >> #
    for i in range(1, num + 1):

        # << Check if number divided by the instance (number) has a remainder or not, if it doesn't, it is a factor >> #
        if num % i == 0:
            factorlist.append(i)

    print(f"The factors of {num} is {factorlist}")

    # << Return the list >> #
    return(factorlist)

# << Challenge 5 >> #
def GCF(x, y):
    XFactors = factorout(x)
    YFactors = factorout(y)
    GreatestCF = 0

    for factor in XFactors:
        if factor in YFactors:
            GreatestCF = max(GreatestCF, factor)

    print(f"The Greatest Common Factor Of {x} and {y} is {GreatestCF}")

GCF(345214567344535, 57543536575235)