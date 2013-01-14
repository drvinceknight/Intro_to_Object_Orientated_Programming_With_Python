#Basic statement:
print "Hello world!"
#That was a command, this is a comment
print "Writing comments is awesome"  # Here is another comment...

#Getting help:
help("range")

#Charachter variables:
string = "Hello world"
print string

#Numeric variables:
num_1 = 2
num_2 = 3.5
print num_1 + num_2

#We define a variable called String:
string = "My name is Vince"
#Let's print the 5th letter of String (Note that Python starts counting at 0):
print string[4]

#We print the elements in position 1 to 4 (not included) in String:
print string[1:4]

#We can use the "index" method to find the position of the first occurrence of an element in String:
a = string.index("V")
print a

#If we leave 1 position empty Python returns "everything":
print string[a:]
print string[:a]

#We define a variable called Num:
num = 3
#We can add 1 to Num in 2 ways:
num = num + 1
num += 1
print num

#We can carry out other numeric operations in a similar way:
num -= 2
num *= 3
num **= 2
print num

#Note that we might not get what we expect with division:
num2 = 5
print num / num2
#Try (there are other ways):
print num / float(num2)

#We define a variable guess to be inputted at the prompt:
guess = input('Guess a number:')
#We use the if statement to check a condition.
#We're using modulo arithmetic to check if the guess is a multiple of 2:
if guess % 2 == 0:
    #If the guess is a multiple of 2 we print a statement to the prompt:
        print "Your guess was an even number"
        #If the guess is not a multiple of 2 we print a different statement:
else:
        print "Your guess was an odd number"

#We set an initial guess:
correct_guess = 9
#We define a variable guess through input at the prompt:
guess = input('What is my favorite number:')
#We use the while command to repeatedly evaluate whether or not the user guesses correctly.
while guess != correct_guess:
#We embed an if statement within this while loop to help the user guess correctly.
    if guess > correct_guess:
        guess = input('Your previous guess was too high:')
    else:
        guess = input('Your previous guess was too low:')
#Note the indentation levels indicating that we are outside of the while loop.
print "Great guess!"

#The for statement is a very powerful statement that allows us to loop over elements in a list (we will look at lists closely shortly).
for i in [1, 2, 3, 4]:
        print i

#We can iterate over all types of variables:
for i in ["Queueing Theory", "Game Theory", "Inventory Theory", "Reliability Theory", "Project Management", "Decision Analysis"]:
#We check if the string 'Theory' is contained within each element of the above list:
    if "Theory" in i:
        print i


#To create a function we use the 'def' statement:
def hi():
    """
            This function simply prints a short statement. (This is a shorter way of writing longer comments, it's good practice to always include a description of what a function does).
    """
    print "Hello everybody!"

hi()


def fibonacci_function(n):
    """
    This returns the nth Fibonacci number.
    """
    #We have 2 statements to check initial conditions
    if n == 0:
        return 1
    #We use the 'else if' statement: "elif":
    elif n == 1:
        return 1
    a, b = 0, 1
    #We use a for statement with the range command.
    for k in range(n):
        #We here use simultaneous assignment:
        a, b = b, a + b
    return b

#We define a list using the range command that gives us a collection of integers:
my_list = range(6)
print my_list
#We can index elements of a list in the same way we indexed strings:
print my_list[0]
#An important 'method' that can be used on lists is the 'append' method which lets us add an object to a list:
my_list.append(100)
print my_list

#A bad phonebook:
pb = [["Vince", 3], ["Zoe", 2], ["Julien", 6], ["Thomas", 10], ["Mike", 1], ["Matt", 4]]

#A good phonebook:
pb = {"Vince": 3, "Zoe": 2, "Julien": 6, "Thomas": 10, "Mike": 1, "Matt": 4}

#Creating a dictionary:
my_dictionary = {"Vince": 3, "Zoe": 2, "Julien": 6, "Thomas": 10, "Mike": 1, "Matt": 4}
#Adding 10 to the value associated to the key: "Zoe":
my_dictionary["Zoe"] += 10
print my_dictionary
