# << Contains All Challenge Codes >> # 
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
{Name1} did not expect much to happen but then they triped on a {Noun1} and fell down the stairs.
{Name1} woke up in a hostipial shortly after but {Verb2} away back to school""")
    
# << Challenge 2 >> #
def odd(num):
    if num%2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

# << Challenge 3 >> #
def bill():
    pass

# << Challenge 4 >> #
def factorout(num):
    factorlist = []

    for i in range(1, num + 1):
        if num % i == 0:
            factorlist.append(i)

    print(f"The factors of {num} is {factorlist}")

# << Challenge 5 >> #
def GCF(x, y):
    pass

MadLibs()