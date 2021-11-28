import pytest

import os


from ls_history import addToHistory

# ====================================
# ==== test setup ====================
# ====================================
 
def history_test_one(iterations, lSystem):
    variables = ["A", "B"]
    constants = ["+", "-"]
    axiom = "A"
    rules = {
        "A": "B-",
        "B": "AB+"
    }
    translations = {
        "A": ["nop"],
        "B": ["nop", "nop"]
    }
    line, timestamp = addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    return line, timestamp

def history_test_two(iterations, lSystem):
    variables = ["A", "B", "C"]
    constants = ["+", "-", "|"]
    axiom = "A"
    rules = {
        "A": "B-",
        "B": "AB+"
    }
    translations = {
        "A": ["nop", "color", "black"],
        "B": ["nop"]
    }
    line, timestamp = addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    return line, timestamp

def history_test_three(iterations, lSystem):
    
    variables = ["A", "B", "C"]
    constants = ["+", "-", "|"]
    axiom = "A"
    rules = {
        "A": "B-",
        "B": "AB+"
    }
    translations = {
        "A": ["nop", "color", "black"],
        "B": ["nop"]
    }
    
    if os.path.exists("History.txt"):
        with open("History.txt", "r") as readFile:
            content = readFile.readlines()
        
        os.remove("History.txt")
    
        line, timestamp = addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    
        with open("History.txt", "w") as writeFile:
            writeFile.writelines(content)
            
    else:
        line, timestamp = addToHistory(variables, constants, axiom, rules, translations, iterations, lSystem)
    
    return line, timestamp

# ===================================
# ==== actual tests =================
# ===================================

# === test 1 ===
def test_one_1():
    line, timestamp = history_test_one(0, "A")
    assert line == "\n" + timestamp + "\t['A', 'B']\t['+', '-']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop'], 'B': ['nop', 'nop']}\t0\tA"
    
def test_one_2():
    line, timestamp = history_test_one(1, "B-")
    assert line == "\n" + timestamp + "\t['A', 'B']\t['+', '-']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop'], 'B': ['nop', 'nop']}\t1\tB-"
    
def test_one_3():
    line, timestamp = history_test_one(2, "AB+-")
    assert line == "\n" + timestamp + "\t['A', 'B']\t['+', '-']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop'], 'B': ['nop', 'nop']}\t2\tAB+-"
    
def test_one_4():
    line, timestamp = history_test_one(3, "B-AB++-")
    assert line == "\n" + timestamp + "\t['A', 'B']\t['+', '-']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop'], 'B': ['nop', 'nop']}\t3\tB-AB++-"
    
def test_one_5():
    line, timestamp = history_test_one(4, "AB+-B-AB+++-")
    assert line == "\n" + timestamp + "\t['A', 'B']\t['+', '-']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop'], 'B': ['nop', 'nop']}\t4\tAB+-B-AB+++-"

# === test 2 ===
def test_two_1():
    line, timestamp = history_test_two(0, "A")
    assert line == "\n" + timestamp + "\t['A', 'B', 'C']\t['+', '-', '|']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop', 'color', 'black'], 'B': ['nop']}\t0\tA"
    
def test_two_2():
    line, timestamp = history_test_two(42, "vkdrvfsdrjkdfrenj cfdk fdk jfkndklji kids klm rji klklio")
    assert line == "\n" + timestamp + "\t['A', 'B', 'C']\t['+', '-', '|']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop', 'color', 'black'], 'B': ['nop']}\t42\tvkdrvfsdrjkdfrenj cfdk fdk jfkndklji kids klm rji klklio"
    
def test_two_3():
    line, timestamp = history_test_two(9999999999999999999999999999999999999989, "A")
    assert line == "\n" + timestamp + "\t['A', 'B', 'C']\t['+', '-', '|']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop', 'color', 'black'], 'B': ['nop']}\t9999999999999999999999999999999999999989\tA"

def test_two_4():
    line, timestamp = history_test_two(1, "\\")
    assert line == "\n" + timestamp + "\t['A', 'B', 'C']\t['+', '-', '|']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop', 'color', 'black'], 'B': ['nop']}\t1\t\\"
    
def test_three_1():
    line, timestamp = history_test_three(0, "A")    
    assert line == "\n" + timestamp + "\t['A', 'B', 'C']\t['+', '-', '|']\tA\t{'A': 'B-', 'B': 'AB+'}\t{'A': ['nop', 'color', 'black'], 'B': ['nop']}\t0\tA"
