import re

print("hee hee\n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    if previous == 0:

        # Input numbers and the arithmetic operations like "+, -, /, *, etc".
        equation = input("Enter equation: ")
    else:

        # Limited number length for decimal and float numbers
        if len(str(previous)) > 15 and "." in str(previous):
            previous = format(previous, ".15g")
            equation = input(str(previous))

            # remove the "0" from the last number of float or decimal numbers
            # so it will remove the last "0" from this kinda things: "0.10", "0.8273640", "1123.1239870"
            # The output will be: "0.1", "0.827364", "1123.123987"
            if str(previous).endswith("0"):
                equation = input(str(previous).rstrip("0"))

        # remove the ".0" from the last number of float or decimal numbers
        # so it will remove the ".0" from this kinda things: "1.0", "231.0", "-9.0"
        # The output will be: "1", "231", "-9" something like that.
        elif str(previous).endswith(".0"):
            previous = str(previous)[:-2]
            equation = input(str(previous))
        else:
            equation = input(str(previous))

    # Exit the program by type "quit", it's not good for real calculator, but yeah its just for fun.
    if equation == "quit":
        print("Goodbye, human.")
        run = False
    else:

        # These characters: '[a-zA-Z,:()"]' will not be displayed from the output
        equation = re.sub('[a-zA-Z,:()"]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
