# Currency-Formatter

A Simple GUI enabled Application to Format the Amount into US Currency Format

Here are some of the Conditions that it Satisfies:
The $ prefix is added to each formatted output
The cents must be rounded to 2 decimal places
In case the decimal is .99, it will not be rounded off to 1.00
0 is a valid input and returns $0.00
Negative numbers are also valid. Follows the same rules
Uses Comma as the separator. In US Currency the comma occurs after every 3 characters
If an input that is not a valid number is passed, the output is NaN
