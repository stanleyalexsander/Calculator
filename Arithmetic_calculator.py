import re

print("heehee\n")

previous = 0
run = True


def perform_math():
    global run
    global previous
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        if len(str(previous)) > 15 and "." in str(previous):
            previous = format(previous, ".15g")
            equation = input(str(previous))
            if str(previous).endswith("0"):
                equation = input(str(previous).rstrip("0"))
        elif str(previous).endswith(".0"):
            previous = str(previous)[:-2]
            equation = input(str(previous))
        else:
            equation = input(str(previous))

    if equation == "quit":
        print("Goodbye, human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,:()"]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()
