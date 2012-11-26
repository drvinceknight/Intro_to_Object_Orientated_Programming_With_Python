#Group Project

---

In groups of 4 attempt to write code that would solve the following problem.

##Company:

Supermarket

##Required product:

Program to evaluate total income from sales and keep count of loyalty points acquired by a given customer if he/she signs up to the loyalty program.

##Parameters:

The input to the problem is 3 csv files:

- Stock report:

    - Department
    - Name of roduct
    - Price of product
    - Loyalty points corresponding to product

- Sales history:

    - Date
    - Loyalty number (0 if not signed up to loyalty program)
    - List of products bought

- Promotions history:

    - Date
    - Department
    - Promotion

##Particularities that need to be taken in to account:

- Every department is capable of assigning a particular sale. The code you write must be able to handle the application of a particular sale on any given day.
- The product list can be updated on any given day. As such your code must be able to handle a change of product attribute but also the possibility for new departments.
- Your code must be generic so as to handle different combinations of the three above files.

##Summary:

The following picture summarises your challenge:

![The underlying structure](https://github.com/drvinceknight/Intro_to_Object_Orientated_Programming_With_Python/blob/master/Challenge/Supermarket_Challenge.png?raw=true)

##Evaluation:

Your code will be evaluated by placing it in a directory containing 3 files:

- 'Stock_Report.csv'
- 'Sale_History.csv'
- 'Promotions_History.csv'

Your code should print the sales taken to screen and output a csv file containing the Loyalty points information.

Your code will be evaluated in terms of:

- Precision (does it work and if so is it correct? - This is an objective criteria)
- Performance (how fast is it? how does it handle bugs? - This is an objective criteria)
- Time taken to submit solution (This is an objective criteria)
- Clarity (is it well written with comments in code? - This is a subjective criteria)

##Suggestion:

I suggest you proceed by clearly defining independent programming tasks and attempting to work independently whilst ensuring that each piece of code produced is capable of talking to each other piece.
