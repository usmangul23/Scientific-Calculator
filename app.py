import streamlit as st
import math

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x):
    if x > 0:
        return math.log10(x)
    return "Error! Logarithm undefined for non-positive values."

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error! Factorial undefined for negative numbers."
    return math.factorial(x)

# Streamlit app
st.title("Scientific Calculator")

# Input from user
operation = st.selectbox("Select an operation", 
                         ["Add", "Subtract", "Multiply", "Divide", "Square Root", 
                          "Exponentiation (x^y)", "Logarithm", "Sine", "Cosine", 
                          "Tangent", "Factorial"])

if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponentiation (x^y)"]:
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
else:
    num1 = st.number_input("Enter the number", value=0.0)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Square Root":
        result = square_root(num1)
    elif operation == "Exponentiation (x^y)":
        result = power(num1, num2)
    elif operation == "Logarithm":
        result = logarithm(num1)
    elif operation == "Sine":
        result = sine(num1)
    elif operation == "Cosine":
        result = cosine(num1)
    elif operation == "Tangent":
        result = tangent(num1)
    elif operation == "Factorial":
        result = factorial(int(num1))

    st.write(f"The result is: {result}")
