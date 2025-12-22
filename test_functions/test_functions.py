def test(target, actual):
    if target == actual:
        print(f"\x1b[32m✔ {target}={actual}\x1b[0m", flush=True)
        return True
    else:
        print(f"\x1b[31m✘ {target}≠{actual}\x1b[0m", flush=True)
        return False

def test_tuples(tuples):
    correct = 0
    for target, actual in tuples:
        correct += test(target, actual)
    
    if len(tuples) == correct:
        print(f"\x1b[1;92mCorrect: {correct}/{len(tuples)}\x1b[0m", flush=True)
        return True
    else:
        print(f"\x1b[1;91mCorrect: {correct}/{len(tuples)}\x1b[0m", flush=True)
        return False

def test_functions(functions):
    correct = 0
    for function in functions:
        print(f"{function.__name__}()", flush=True)
        correct += function()

    if len(functions) == correct:
        return True
    else:
        return False
