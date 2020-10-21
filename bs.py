import random
import os
import time
abc = "abcdefghjiklmnopqrstuvwxyz"
nums = "0123456789"
basic = """
i = 0
ram = [x-x for x in range(1024)]
"""


class File:
    def __init__(self, name):
        self.name = name
        self.file = open(self.name+".py", "a")
        self.file.truncate(0)

    def write(self, string: str):
        self.file.write(string+"\n")


def compile_file(file, serial: str = None):
    compile_source(open(file, "r").read(), serial)


def compile_source(source: str, serial: str = None):
    t1 = time.time()
    print(f"BS Compiler v0.285 § Initializing the compiler @ {os.getcwd()}")
    if serial is None:
        print("Generating serial;")
        serial = [f for f in [random.choice(abc+nums) for x in range(10)] if random.randint(1, 2) == 2]
        serial_filtered = ""
        for i in serial:
            serial_filtered += i
        print("OK")
    else:
        print("Using specified serial;")
        serial_filtered = serial
        print("OK")

    print(f"Making .py with name {serial_filtered}.py @ {os.getcwd()} ;")
    file = File(serial_filtered)
    print("OK")
    print("Appending language dependant variables;")
    file.write(basic)
    print("OK")
    print("Setting compiler variables;")
    loops = False
    useless_operators = [" ", "\t", "\n", "\a", "\\", "\f"]
    collected = ""
    print("OK")
    print("Extracting debug info from source;")
    lenght = len(source)
    print("OK")
    print(f"INFO: {lenght}(chr)")
    print(" == BEGIN COMPILE ==")
    for letter in source:
        if loops:
            if letter == "]":
                loops = False
                file.write("while ram[i] > 0:\n"+collected)
                collected = ""
            elif letter == ">":
                collected += "    i += 1\n"
            elif letter == "<":
                collected += "    i -= 1\n"
            elif letter == "+":
                collected += "    ram[i] += 1\n"
            elif letter == "-":
                collected += "    ram[i] -= 1\n"
            elif letter == "*":
                collected += "    ram[i] *= ram[i]\n"
            elif letter == "/":
                collected += "    ram[i] /= ram[i]\n"
            elif letter == ".":
                collected += "    print(ram[i])\n"
            elif letter == "|":
                collected += "    print(chr(ram[i]))\n"
            elif letter in useless_operators:
                pass
            else:
                raise SyntaxError(f"{letter} is not an operator")

        else:
            if letter == ">":
                file.write("i += 1")
            elif letter == "<":
                file.write("i -= 1")
            elif letter == "+":
                file.write("ram[i] += 1")
            elif letter == ",":
                file.write("ram[i] = input(chr(ram[i]))")
            elif letter == "-":
                file.write("ram[i] -= 1")
            elif letter == "[":
                loops = True
            elif letter == "*":
                file.write("ram[i] *= ram[i]")
            elif letter == "/":
                file.write("ram[i] /= ram[i]")
            elif letter == ".":
                file.write("print(ram[i])")
            elif letter == "|":
                file.write("print(chr(ram[i]))")
            elif letter in useless_operators:
                pass
            else:
                raise SyntaxError(f"{letter} is not an operator")
    print(" == END COMPILE ==")
    print(f"Process finished in: {time.time()-t1}(s)")
