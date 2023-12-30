"Module docstring"
def add(number_1, number_2):
    "This is a fantastic function to try Pylint"
    return number_1 + number_2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")

