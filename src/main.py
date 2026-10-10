from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Debashis Roy")
print("Date:", date.today())

print("10 + 5 =", add(10, 5))
print("10 - 5 =", subtract(10, 5))
print("10 * 5 =", multiply(10, 5))
try:
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))
except ValueError as e:
    print("Error:", e)
