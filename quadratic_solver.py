import streamlit as st
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two real and distinct roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: {real_part}+{imaginary_part}i and {real_part}-{imaginary_part}i"

st.title("Quadratic Equation Solver")

st.write("A quadratic equation is of the form ax² + bx + c = 0")

a = st.number_input("Enter the coefficient a", value=1.0)
b = st.number_input("Enter the coefficient b", value=0.0)
c = st.number_input("Enter the coefficient c", value=0.0)

if st.button("Solve"):
    if a == 0:
        st.write("Coefficient 'a' cannot be zero in a quadratic equation.")
    else:
        solution = solve_quadratic(a, b, c)
        st.write(solution)
