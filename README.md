# Calculator App

This is a simple calculator application built using Python and the Tkinter library. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation.

## Prerequisites
Before running the application, ensure that you have the following:

Python 3.x installed on your system

## Getting Started

Clone the repository:
```git clone https://github.com/In-Time-Tec/python-calculator```

Navigate to the project directory:
```cd python-calculator```

Create a virtual environment (optional but recommended):
```python3 -m venv venv```

Activate the virtual environment:

For Windows:
```codevenv\Scripts\activate```

For macOS and Linux:
```source venv/bin/activate```

Run the application:
```python calculator.py```


### Fixing Broken Code
The provided code has a few issues that need to be addressed. Here are some things to look out for.

Implement the square_root function:

Add the necessary logic to calculate the square root of the current value in the entry.
Clear the entry and display the result.
If the current value is negative, display an error message.


Implement the percentage function:

Add the logic to calculate the percentage of the current value in the entry.
Clear the entry and display the result as a decimal (e.g., 0.5 for 50%).


Update the calc function:

Handle any additional exceptions that may occur during the evaluation of the input expression.
Display appropriate error messages for invalid input or unsupported operations.


Test the calculator thoroughly:

Verify that all the buttons and operations work as expected.
Test edge cases and error scenarios to ensure proper handling.



### Usage

Click on the number buttons to input values.
Use the arithmetic operation buttons (+, -, *, /, ^) to perform calculations.
Press the '=' button to evaluate the expression and display the result.
Click the 'C' button to clear the current entry.
Use the '<-' button to delete the last character in the entry.
Click the 'Quit' button to exit the application.