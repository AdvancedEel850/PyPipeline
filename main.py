def main():
    test_runner()
    print("All test pass!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        c = a/b

    except ZeroDivisionError:
        c = 0

    return c

def multiply(a, b):
    return a*b

def test_runner():
    add_test_small()
    add_test_large()
    sub_test_small()
    sub_test_large()
    div_test_small()
    div_test_large()
    dive_test_by_zero()
    mult_test_small()
    mult_test_large()

def add_test_small():
    # Setup
    a = 1
    b = 2
    # Exercise
    c = add(a,b)
    # Verify
    assert(c == 3)
    # teardown

def add_test_large():
    # Setup
    a = 100
    b = 229
    # Exercise
    c = add(a,b)
    # Verify
    assert(c == 329)
    # teardown

def sub_test_small():
    # Setup
    a = 1
    b = 2
    # Exercise
    c = subtract(a,b)
    # Verify
    assert(c == -1)
    # teardown

def sub_test_large():
    # Setup
    a = 229
    b = 100
    # Exercise
    c = subtract(a,b)
    # Verify
    assert(c == 129)
    # teardown

def div_test_small():
    # Setup
    a = 1
    b = 2
    # Exercise
    c = divide(a,b)
    # Verify
    assert(c == .5)
    # teardown

def div_test_large():
    # Setup
    a = 50
    b = 20
    # Exercise
    c = divide(a,b)
    # Verify
    assert(c == 2.5)
    # teardown

def dive_test_by_zero():
    # Setup
    a = 1
    b = 0
    # Exercise
    c = divide(a,b)
    # Verify
    assert(c == 0)
    # teardown

def mult_test_small():
    # Setup
    a = 1
    b = 2
    # Exercise
    c = multiply(a,b)
    # Verify
    assert(c == 2)
    # teardown

def mult_test_large():
    # Setup
    a = 100
    b = 224
    # Exercise
    c = multiply(a,b)
    # Verify
    assert(c == 22400)
    # teardown

main()