import math
# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(1.234.upper())

# KeyError
def produce_key_error():
    student = {
        "name": "Keiko",
        "course": "CFG",
    }
    print(student["age"])

# IndexError
def produce_index_error():
    letters = ["A", "B"]
    print(letters[3])

# NameError
def produce_name_error():
    name = "Keiko"
    print(address)

# UnboundLocalError
def produce_unbound_local_error():
    print(score)
    score = 100

# TypeError
def produce_type_error():
    score = 100
    name = "Keiko"
    myResult = score / name

# ValueError
def produce_value_error():
    math.sqrt(-3)


# ZeroDivisionError
def produce_zero_division_error():
    10 / 0


# OverflowError
def produce_overflow_error():
    print(math.exp(100000000))


# FileNotFoundError
def produce_file_not_found_error():
    f = open("test.txt", "r")

# UnicodeEncodeError
def produce_unicode_encode_error():
    u"\u0411".encode("iso-8859-15")

# ModuleNotFoundError
def produce_module_not_found_error():
    import NumPyyy


# ImportError
def produce_import_error():
    import NumPyyy
