# EMI-_LOAN-_CAL
A SIMPLE EMI LOAN CALCULATOR USING PYTHON 


👉#Features

Accepts user input for loan amount, interest rate, and loan tenure.

👉#Calculates:

Monthly payment (EMI)

Total amount payable

Total interest paid

Handles cases where the interest rate is 0%.

Provides formatted output for better readability.

👉 FORMULAS USED

For loans with interest:

EMI = (P * r) / (1 - (1 + r) ** -n)

where:

P = Principal loan amount

r = Monthly interest rate (Annual rate / 12 / 100)

n = Total number of months

For loans with 0% interest, EMI is simply:

EMI = Principal / Total months

#Installation & Usage

👉Prerequisites

Python 3.x installed on your system

Running the Program

Download or clone this repository.

Open a terminal or command prompt and navigate to the project directory.

#Run the script using:

python loan_calculator.py

Enter the required inputs when prompted.

The program will display the calculated values.

#Example Input & Output

👉Input:
Enter loan amount: 50000
Enter annual interest rate (in %): 5
Enter loan tenure (in years): 2

👉Output:
Monthly Payment: 2197.42
Total Payment: 52738.10
Total Interest: 2738.10

👉License
This project is open-source and free to use for educational purposes.
