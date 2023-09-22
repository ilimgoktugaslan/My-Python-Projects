from tkinter import *
import unittest

def write(x, entry):
    s = len(entry.get())
    entry.insert(s, str(x))

def operations(x, entry):
    global calculation, n1
    calculation = x
    n1 = float(entry.get())
    entry.delete(0, "end")

def calculate(entry):
    global calculation, n1
    n2 = float(entry.get())
    result = 0
    if calculation == 0:
        result = n1 + n2
    elif calculation == 1:
        result = n1 - n2
    elif calculation == 2:
        result = n1 * n2
    elif calculation == 3:
        result = n1 / n2
    entry.delete(0, "end")
    entry.insert(0, str(result))

class CalculatorTest(unittest.TestCase):
    def test_write(self):
        entry = Entry()
        write(5, entry)
        self.assertEqual(entry.get(), "5")

    def test_operations(self):
        entry = Entry()
        operations(2, entry)
        self.assertEqual(calculation, 2)

    def test_calculate(self):
        entry = Entry()
        global calculation, n1
        calculation = 0
        n1 = 5
        entry.insert(0, "10")
        calculate(entry)
        self.assertEqual(entry.get(), "15")

if __name__ == "__main__":
    unittest.main()
